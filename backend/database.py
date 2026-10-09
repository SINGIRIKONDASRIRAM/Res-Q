"""
Database Store & Supabase Connection Handler
Handles live Supabase connection with local state fallback to ensure 
instant, reliable, robust operation out-of-the-box.
"""

import os
import uuid
from datetime import datetime
from typing import List, Dict, Any
from dotenv import load_dotenv

load_dotenv()

SUPABASE_URL = os.getenv("VITE_SUPABASE_URL", "")
SUPABASE_KEY = os.getenv("SUPABASE_SERVICE_ROLE_KEY", os.getenv("VITE_SUPABASE_ANON_KEY", ""))

supabase_client = None
if SUPABASE_URL and SUPABASE_KEY:
    try:
        from supabase import create_client
        supabase_client = create_client(SUPABASE_URL, SUPABASE_KEY)
        print(" Connected to Supabase PostgreSQL database.")
    except Exception as e:
        print(f" Supabase init notice: {e}. Defaulting to hybrid memory database engine.")

# In-Memory Realistic Demo Storage Engine
INITIAL_DISASTERS = [
    {
        "id": "d101",
        "name": "Cyclone Vardah Relief & Storm Emergency",
        "type": "Cyclone",
        "location": "Coastal Zone - East Bay",
        "severity": "Critical",
        "description": "Category 4 tropical cyclone causing coastal inundation, power grid breakdown, and mass displacement.",
        "date": "2026-08-10",
        "status": "Active",
        "created_at": "2026-08-10T08:00:00Z"
    },
    {
        "id": "d102",
        "name": "River Kaveri Flash Flooding",
        "type": "Flood",
        "location": "Central River Basin & Lowlands",
        "severity": "High",
        "description": "Heavy monsoon discharge inundating 12 low-lying residential sectors and agricultural blocks.",
        "date": "2026-08-11",
        "status": "Active",
        "created_at": "2026-08-11T09:30:00Z"
    },
    {
        "id": "d103",
        "name": "Western Ghats Landslide Emergency",
        "type": "Landslide",
        "location": "Mountain Ridge Sector 4",
        "severity": "Medium",
        "description": "Mudslide blocking national arterial highways and cutting off communications to remote villages.",
        "date": "2026-08-12",
        "status": "Monitoring",
        "created_at": "2026-08-12T14:15:00Z"
    }
]

INITIAL_AREAS = [
    {
        "id": "area_hyd_101",
        "disaster_id": "d101",
        "area_name": "Hitec City IT Corridor",
        "population": 12000,
        "severity": "High",
        "medical_cases": 85,
        "vulnerable_population": 400,
        "latitude": 17.4474,
        "longitude": 78.3762,
        "food_required": 1500,
        "water_required": 3000,
        "medicine_required": 200,
        "priority_score": 88,
        "status": "Active Threat",
        "source": "AI Sensor Network"
    },
    {
        "id": "area_hyd_102",
        "disaster_id": "d101",
        "area_name": "Gachibowli Financial District",
        "population": 8500,
        "severity": "Medium",
        "medical_cases": 30,
        "vulnerable_population": 250,
        "latitude": 17.4400,
        "longitude": 78.3489,
        "food_required": 800,
        "water_required": 1600,
        "medicine_required": 80,
        "priority_score": 65,
        "status": "Active Threat",
        "source": "Satellite Scan"
    },

    {
        "id": "a1",
        "disaster_id": "d101",
        "area_name": "Area A - Coastal Sector 1",
        "population": 8500,
        "severity": "Critical",
        "medical_cases": 280,
        "vulnerable_population": 2100,
        "latitude": 13.0827,
        "longitude": 80.2707,
        "food_required": 2200,
        "water_required": 3500,
        "medicine_required": 450,
        "priority_score": 94.2,
        "status": "Critical"
    },
    {
        "id": "a2",
        "disaster_id": "d101",
        "area_name": "Area B - North Harbor",
        "population": 6200,
        "severity": "Critical",
        "medical_cases": 190,
        "vulnerable_population": 1400,
        "latitude": 13.1200,
        "longitude": 80.2900,
        "food_required": 1800,
        "water_required": 2600,
        "medicine_required": 320,
        "priority_score": 87.5,
        "status": "Critical"
    },
    {
        "id": "a3",
        "disaster_id": "d102",
        "area_name": "Area C - Riverbed Township",
        "population": 9400,
        "severity": "High",
        "medical_cases": 140,
        "vulnerable_population": 1800,
        "latitude": 13.0400,
        "longitude": 80.2100,
        "food_required": 2500,
        "water_required": 4000,
        "medicine_required": 280,
        "priority_score": 78.4,
        "status": "High"
    },
    {
        "id": "a4",
        "disaster_id": "d102",
        "area_name": "Area D - South Delta Colony",
        "population": 4800,
        "severity": "High",
        "medical_cases": 95,
        "vulnerable_population": 900,
        "latitude": 12.9800,
        "longitude": 80.2400,
        "food_required": 1200,
        "water_required": 2000,
        "medicine_required": 160,
        "priority_score": 71.1,
        "status": "High"
    },
    {
        "id": "a5",
        "disaster_id": "d101",
        "area_name": "Area E - Fisherman Island",
        "population": 3100,
        "severity": "Critical",
        "medical_cases": 125,
        "vulnerable_population": 750,
        "latitude": 13.1500,
        "longitude": 80.3100,
        "food_required": 1100,
        "water_required": 1600,
        "medicine_required": 210,
        "priority_score": 89.0,
        "status": "Critical"
    },
    {
        "id": "a6",
        "disaster_id": "d103",
        "area_name": "Area F - Hill Pass Ridge",
        "population": 2400,
        "severity": "Medium",
        "medical_cases": 45,
        "vulnerable_population": 420,
        "latitude": 13.0100,
        "longitude": 80.1500,
        "food_required": 800,
        "water_required": 1200,
        "medicine_required": 90,
        "priority_score": 56.3,
        "status": "Medium"
    },
    {
        "id": "a7",
        "disaster_id": "d102",
        "area_name": "Area G - Western Basin Slums",
        "population": 7100,
        "severity": "High",
        "medical_cases": 160,
        "vulnerable_population": 1600,
        "latitude": 13.0600,
        "longitude": 80.1800,
        "food_required": 2100,
        "water_required": 3100,
        "medicine_required": 240,
        "priority_score": 76.8,
        "status": "High"
    },
    {
        "id": "a8",
        "disaster_id": "d103",
        "area_name": "Area H - Highland Village",
        "population": 1800,
        "severity": "Low",
        "medical_cases": 15,
        "vulnerable_population": 220,
        "latitude": 13.1800,
        "longitude": 80.1200,
        "food_required": 500,
        "water_required": 800,
        "medicine_required": 40,
        "priority_score": 38.5,
        "status": "Low"
    },
    {
        "id": "a9",
        "disaster_id": "d101",
        "area_name": "Area I - Industrial Belt Shelter",
        "population": 5500,
        "severity": "High",
        "medical_cases": 110,
        "vulnerable_population": 850,
        "latitude": 13.1000,
        "longitude": 80.2200,
        "food_required": 1600,
        "water_required": 2400,
        "medicine_required": 180,
        "priority_score": 68.2,
        "status": "High"
    },
    {
        "id": "a10",
        "disaster_id": "d102",
        "area_name": "Area J - Central Railway Depot",
        "population": 3900,
        "severity": "Medium",
        "medical_cases": 50,
        "vulnerable_population": 500,
        "latitude": 13.0750,
        "longitude": 80.2600,
        "food_required": 950,
        "water_required": 1400,
        "medicine_required": 110,
        "priority_score": 52.1,
        "status": "Medium"
    }
]

INITIAL_RESOURCES = [
    # Essential Supplies
    {"id": "r1", "resource_name": "Food Rations Packets", "resource_type": "Food", "category": "Essential Supplies", "quantity_available": 185000, "quantity_allocated": 11200, "unit": "packets", "location": "Central Logistics Hub", "minimum_threshold": 3000},
    {"id": "r2", "resource_name": "Potable Water Cans (20L)", "resource_type": "Drinking Water", "category": "Essential Supplies", "quantity_available": 260000, "quantity_allocated": 17500, "unit": "cans", "location": "Water Purification Base A", "minimum_threshold": 5000},
    {"id": "r3", "resource_name": "Essential Trauma & Antibiotic Kits", "resource_type": "Medicine", "category": "Essential Supplies", "quantity_available": 28000, "quantity_allocated": 1650, "unit": "kits", "location": "Apex Medical Depot", "minimum_threshold": 500},
    {"id": "r4", "resource_name": "Thermal Wool Blankets", "resource_type": "Blankets", "category": "Essential Supplies", "quantity_available": 45000, "quantity_allocated": 2200, "unit": "pieces", "location": "Central Logistics Hub", "minimum_threshold": 1000},
    {"id": "r5", "resource_name": "Emergency Clothing Kits", "resource_type": "Clothes", "category": "Essential Supplies", "quantity_available": 32000, "quantity_allocated": 1400, "unit": "sets", "location": "Central Logistics Hub", "minimum_threshold": 800},
    # Emergency Equipment
    {"id": "r6", "resource_name": "Field Trauma First Aid Kits", "resource_type": "First Aid Kits", "category": "Emergency Equipment", "quantity_available": 12000, "quantity_allocated": 750, "unit": "kits", "location": "Apex Medical Depot", "minimum_threshold": 200},
    {"id": "r7", "resource_name": "High-Pressure Oxygen Cylinders", "resource_type": "Oxygen Cylinders", "category": "Emergency Equipment", "quantity_available": 6500, "quantity_allocated": 410, "unit": "cylinders", "location": "Apex Medical Depot", "minimum_threshold": 100},
    {"id": "r8", "resource_name": "Heavy-Duty Hydraulic Rescue Cutters", "resource_type": "Rescue Equipment", "category": "Emergency Equipment", "quantity_available": 1400, "quantity_allocated": 95, "unit": "sets", "location": "NDRF Armory", "minimum_threshold": 30},
    {"id": "r9", "resource_name": "Mobile Diesel Generators 50kW", "resource_type": "Generators", "category": "Emergency Equipment", "quantity_available": 850, "quantity_allocated": 52, "unit": "units", "location": "Power Grid ResQ Base", "minimum_threshold": 15},
    # Human Resources
    {"id": "r10", "resource_name": "Emergency Doctors & Surgeons", "resource_type": "Doctors", "category": "Human Resources", "quantity_available": 65, "quantity_allocated": 48, "unit": "personnel", "location": "District General Hospital", "minimum_threshold": 10},
    {"id": "r11", "resource_name": "Trauma Care Nurses", "resource_type": "Nurses", "category": "Human Resources", "quantity_available": 140, "quantity_allocated": 98, "unit": "personnel", "location": "District General Hospital", "minimum_threshold": 25},
    {"id": "r12", "resource_name": "NDRF Search & Rescue Teams", "resource_type": "Rescue Teams", "category": "Human Resources", "quantity_available": 24, "quantity_allocated": 16, "unit": "teams", "location": "National Response Camp", "minimum_threshold": 5},
    {"id": "r13", "resource_name": "Civil Defense Volunteers", "resource_type": "Volunteers", "category": "Human Resources", "quantity_available": 450, "quantity_allocated": 280, "unit": "volunteers", "location": "Civic Staging Ground", "minimum_threshold": 50},
    # Vehicles
    {"id": "r14", "resource_name": "Advanced Life Support Ambulances", "resource_type": "Ambulance", "category": "Vehicles", "quantity_available": 32, "quantity_allocated": 24, "unit": "vehicles", "location": "Medical Fleet Depot", "minimum_threshold": 6},
    {"id": "r15", "resource_name": "All-Terrain Rescue Vehicles (4x4)", "resource_type": "Rescue Vehicle", "category": "Vehicles", "quantity_available": 28, "quantity_allocated": 19, "unit": "vehicles", "location": "NDRF Armory", "minimum_threshold": 5},
    {"id": "r16", "resource_name": "Heavy Supply Cargo Trucks (10T)", "resource_type": "Supply Truck", "category": "Vehicles", "quantity_available": 40, "quantity_allocated": 27, "unit": "trucks", "location": "Central Logistics Hub", "minimum_threshold": 8},
    {"id": "r17", "resource_name": "Motorized Inflatable Rescue Boats", "resource_type": "Boat", "category": "Vehicles", "quantity_available": 35, "quantity_allocated": 26, "unit": "boats", "location": "Coastal Guard Station", "minimum_threshold": 6}
]

INITIAL_REQUESTS = [
    {"id": "req1", "area_id": "a1", "area_name": "Area A - Coastal Sector 1", "resource_type": "Medicine", "quantity": 150, "urgency": "Critical", "description": "Severe outbreak of waterborne gastroenteritis following floodwaters.", "status": "Pending", "created_at": "2026-08-13T10:15:00Z"},
    {"id": "req2", "area_id": "a2", "area_name": "Area B - North Harbor", "resource_type": "Food", "quantity": 800, "urgency": "Critical", "description": "Relief camp stranded without grain & dry rations.", "status": "Pending", "created_at": "2026-08-13T11:00:00Z"},
    {"id": "req3", "area_id": "a5", "area_name": "Area E - Fisherman Island", "resource_type": "Drinking Water", "quantity": 1200, "urgency": "Critical", "description": "Saline contamination of local wells. Zero potable water remaining.", "status": "Pending", "created_at": "2026-08-13T11:30:00Z"},
    {"id": "req4", "area_id": "a3", "area_name": "Area C - Riverbed Township", "resource_type": "Rescue Teams", "quantity": 3, "urgency": "High", "description": "Structural collapse reported near bridge embankment. 12 trapped.", "status": "Approved", "created_at": "2026-08-13T12:00:00Z"},
    {"id": "req5", "area_id": "a7", "area_name": "Area G - Western Basin Slums", "resource_type": "Ambulance", "quantity": 4, "urgency": "High", "description": "Critical patient transfers needed for elderly flood victims.", "status": "Pending", "created_at": "2026-08-13T12:45:00Z"},
    {"id": "req6", "area_id": "a4", "area_name": "Area D - South Delta Colony", "resource_type": "Generators", "quantity": 2, "urgency": "Medium", "description": "Power grid failed at local community clinic.", "status": "Pending", "created_at": "2026-08-13T13:10:00Z"},
    {"id": "req7", "area_id": "a6", "area_name": "Area F - Hill Pass Ridge", "resource_type": "First Aid Kits", "quantity": 60, "urgency": "Medium", "description": "Landslide trauma injuries requiring basic wound dressing.", "status": "Fulfilled", "created_at": "2026-08-13T09:00:00Z"},
    {"id": "req8", "area_id": "a9", "area_name": "Area I - Industrial Belt Shelter", "resource_type": "Blankets", "quantity": 500, "urgency": "Low", "description": "Overnight temp drops affecting evacuees.", "status": "Pending", "created_at": "2026-08-13T14:00:00Z"},
    {"id": "req9", "area_id": "a10", "area_name": "Area J - Central Railway Depot", "resource_type": "Volunteers", "quantity": 25, "urgency": "Medium", "description": "Assistance needed to unload incoming supply freight trains.", "status": "Pending", "created_at": "2026-08-13T14:30:00Z"},
    {"id": "req10", "area_id": "a1", "area_name": "Area A - Coastal Sector 1", "resource_type": "Oxygen Cylinders", "quantity": 20, "urgency": "Critical", "description": "Emergency ICU ward setup at field hospital.", "status": "Approved", "created_at": "2026-08-13T15:00:00Z"}
]

INITIAL_TEAMS = [
    {"id": "t1", "team_name": "Alpha Medical ResQ-1", "leader": "Dr. Aris Thorne", "members": 8, "specialization": "Medical", "location": "Coastal Sector 1", "status": "On Mission", "assigned_area_id": "a1", "assigned_area_name": "Area A - Coastal Sector 1"},
    {"id": "t2", "team_name": "Bravo NDRF Battalion 4", "leader": "Capt. Rajesh Kumar", "members": 15, "specialization": "Search & Rescue", "location": "Riverbed Township", "status": "Assigned", "assigned_area_id": "a3", "assigned_area_name": "Area C - Riverbed Township"},
    {"id": "t3", "team_name": "Charlie Coast Guard Squad", "leader": "Cmdr. Vikram Sethi", "members": 12, "specialization": "Evacuation", "location": "Fisherman Island", "status": "On Mission", "assigned_area_id": "a5", "assigned_area_name": "Area E - Fisherman Island"},
    {"id": "t4", "team_name": "Delta Hazmat Response", "leader": "Lt. Maya Lin", "members": 6, "specialization": "Hazmat", "location": "Central Depot", "status": "Available", "assigned_area_id": None, "assigned_area_name": None},
    {"id": "t5", "team_name": "Echo General Relief Contingent", "leader": "Sgt. David Miller", "members": 20, "specialization": "General Relief", "location": "North Harbor", "status": "Available", "assigned_area_id": None, "assigned_area_name": None}
]

INITIAL_VEHICLES = [
    {
        "id": "vh_hyd_1",
        "type": "Ambulance",
        "vehicle_id": "AP-09-AMB-101",
        "status": "Idle",
        "latitude": 17.4474,
        "longitude": 78.3762,
        "fuel_level": 85,
        "current_mission_id": None,
        "eta_mins": 0,
        "location": "Hitec City Base"
    },
    {
        "id": "vh_hyd_2",
        "type": "Rescue Boat",
        "vehicle_id": "TS-NDRF-BT-05",
        "status": "En Route",
        "latitude": 17.4320,
        "longitude": 78.3940,
        "fuel_level": 70,
        "current_mission_id": "m202",
        "eta_mins": 12,
        "location": "Durgam Cheruvu"
    },
    {
        "id": "vh_hyd_3",
        "type": "Helicopter",
        "vehicle_id": "IAF-CH-HYD",
        "status": "Idle",
        "latitude": 17.4530,
        "longitude": 78.4640,
        "fuel_level": 100,
        "current_mission_id": None,
        "eta_mins": 0,
        "location": "Begumpet Airport"
    },
    {
        "id": "vh_hyd_4",
        "type": "Supply Truck",
        "vehicle_id": "TS-TRK-900",
        "status": "Idle",
        "latitude": 17.4400,
        "longitude": 78.3489,
        "fuel_level": 95,
        "current_mission_id": None,
        "eta_mins": 0,
        "location": "Gachibowli Base"
    },

    {"id": "v1", "vehicle_id": "AMB-101", "type": "Ambulance", "driver": "K. R. Suresh", "capacity": 2, "location": "Coastal Sector 1", "status": "Assigned", "assigned_area_id": "a1", "assigned_area_name": "Area A - Coastal Sector 1"},
    {"id": "v2", "vehicle_id": "AMB-104", "type": "Ambulance", "driver": "M. Praveen", "capacity": 2, "location": "North Harbor", "status": "In Transit", "assigned_area_id": "a2", "assigned_area_name": "Area B - North Harbor"},
    {"id": "v3", "vehicle_id": "TRK-501", "type": "Supply Truck", "driver": "G. Selvam", "capacity": 10000, "location": "Central Logistics Hub", "status": "Available", "assigned_area_id": None, "assigned_area_name": None},
    {"id": "v4", "vehicle_id": "TRK-508", "type": "Supply Truck", "driver": "P. Ramesh", "capacity": 10000, "location": "Riverbed Township", "status": "Assigned", "assigned_area_id": "a3", "assigned_area_name": "Area C - Riverbed Township"},
    {"id": "v5", "vehicle_id": "BOAT-22", "type": "Boat", "driver": "N. Antony", "capacity": 12, "location": "Fisherman Island", "status": "In Transit", "assigned_area_id": "a5", "assigned_area_name": "Area E - Fisherman Island"},
    {"id": "v6", "vehicle_id": "RES-402", "type": "Rescue Vehicle", "driver": "V. Anand", "capacity": 6, "location": "Western Basin Slums", "status": "Assigned", "assigned_area_id": "a7", "assigned_area_name": "Area G - Western Basin Slums"},
    {"id": "v7", "vehicle_id": "HELI-01", "type": "Helicopter", "driver": "Wg Cmdr R. Sharma", "capacity": 8, "location": "Air Force Staging Hub", "status": "Available", "assigned_area_id": None, "assigned_area_name": None},
    {"id": "v8", "vehicle_id": "TRK-512", "type": "Supply Truck", "driver": "S. Murugan", "capacity": 10000, "location": "Central Logistics Hub", "status": "Available", "assigned_area_id": None, "assigned_area_name": None}
]

INITIAL_ALERTS = [
    {"id": "alt0", "title": "Critical ICU Oxygen Shortage", "message": "Emergency ICU ward at Coastal Sector 1 field hospital reports 0 backup oxygen cylinders. 15 critical patients pending emergency dispatch.", "severity": "Critical", "status": "Active", "created_at": "2026-08-13T17:00:00Z"},
    {"id": "alt1", "title": "Critical Medicine Shortage", "message": "Medicine inventory in Area A - Coastal Sector 1 is below safety threshold (85% deficit). Urgent dispatch recommended.", "severity": "Critical", "status": "Active", "created_at": "2026-08-13T11:20:00Z"},
    {"id": "alt2", "title": "Food Inventory Warning", "message": "Food ration inventory at Central Logistics Hub reached minimum safety threshold (30% capacity remaining).", "severity": "Warning", "status": "Active", "created_at": "2026-08-13T12:00:00Z"},
    {"id": "alt3", "title": "Emergency Request Incoming", "message": "New critical emergency request req10 for Oxygen Cylinders logged by Area A Field Hospital.", "severity": "Emergency", "status": "Active", "created_at": "2026-08-13T15:00:00Z"},
    {"id": "alt4", "title": "Flash Flood Wave Approaching", "message": "Hydrological telemetry indicates a 1.2m surge wave reaching Riverbed Township within 3 hours.", "severity": "Critical", "status": "Active", "created_at": "2026-08-13T16:10:00Z"}
]

INITIAL_REPORTS = []

INITIAL_SAFE_LOCATIONS = [
    # Hospitals & Trauma Centers
    {
        "id": "loc_h1",
        "name": "Apollo Emergency & Trauma Hospital",
        "facility_type": "Hospital",
        "icon": "hospital",
        "latitude": 13.0604,
        "longitude": 80.2496,
        "address": "21 Greams Lane, Thousand Lights",
        "phone": "+91 44 2829 0200",
        "capacity": "250 Emergency Beds",
        "icu_available": 35,
        "status": "Operational 24/7"
    },
    {
        "id": "loc_h2",
        "name": "Government General Hospital & ICU Hub",
        "facility_type": "Hospital",
        "icon": "hospital",
        "latitude": 13.0815,
        "longitude": 80.2777,
        "address": "EVR Periyar Salai, Park Town",
        "phone": "+91 44 2530 5000",
        "capacity": "500 Emergency Beds",
        "icu_available": 60,
        "status": "Operational 24/7"
    },
    {
        "id": "loc_h3",
        "name": "Tambaram District Trauma & Surgical Center",
        "facility_type": "Hospital",
        "icon": "hospital",
        "latitude": 12.9240,
        "longitude": 80.1290,
        "address": "GST Road, Tambaram Sanatorium",
        "phone": "+91 44 2241 8000",
        "capacity": "180 Emergency Beds",
        "icu_available": 20,
        "status": "Operational 24/7"
    },
    {
        "id": "loc_h4",
        "name": "Stanley Medical Apex Trauma Care",
        "facility_type": "Hospital",
        "icon": "hospital",
        "latitude": 13.1030,
        "longitude": 80.2870,
        "address": "Old Jail Road, Royapuram",
        "phone": "+91 44 2528 1351",
        "capacity": "320 Emergency Beds",
        "icu_available": 40,
        "status": "Operational 24/7"
    },
    {
        "id": "loc_h5",
        "name": "Chromepet Emergency Medical Base",
        "facility_type": "Hospital",
        "icon": "hospital",
        "latitude": 12.9510,
        "longitude": 80.1410,
        "address": "Station Road, Chromepet",
        "phone": "+91 44 2265 1122",
        "capacity": "120 Emergency Beds",
        "icu_available": 15,
        "status": "Operational 24/7"
    },
    {
        "id": "loc_h6",
        "name": "MIOT International Trauma Hospital",
        "facility_type": "Hospital",
        "icon": "hospital",
        "latitude": 13.0247,
        "longitude": 80.1785,
        "address": "Mount-Poonamallee Road, Manapakkam / Porur",
        "phone": "+91 44 4200 2288",
        "capacity": "300 Emergency ICU Beds",
        "icu_available": 45,
        "status": "Operational 24/7"
    },
    {
        "id": "loc_h7",
        "name": "Sri Ramachandra Medical Center & Emergency Hub",
        "facility_type": "Hospital",
        "icon": "hospital",
        "latitude": 13.0375,
        "longitude": 80.1412,
        "address": "No.1 Ramachandra Nagar, Porur",
        "phone": "+91 44 4592 8500",
        "capacity": "450 Emergency Beds",
        "icu_available": 55,
        "status": "Operational 24/7"
    },
    {
        "id": "loc_h8",
        "name": "SIMS Super Specialty Emergency Hospital",
        "facility_type": "Hospital",
        "icon": "hospital",
        "latitude": 13.0512,
        "longitude": 80.2120,
        "address": "Metro Station Complex, Vadapalani",
        "phone": "+91 44 2000 2000",
        "capacity": "280 Trauma Beds",
        "icu_available": 30,
        "status": "Operational 24/7"
    },
    {
        "id": "loc_h9",
        "name": "Prashanth Emergency Hospital & Trauma Center",
        "facility_type": "Hospital",
        "icon": "hospital",
        "latitude": 12.9780,
        "longitude": 80.2220,
        "address": "Velachery Main Road, Velachery",
        "phone": "+91 44 4227 7777",
        "capacity": "190 Emergency Beds",
        "icu_available": 25,
        "status": "Operational 24/7"
    },
    {
        "id": "loc_h10",
        "name": "Gleneagles Global Trauma & Emergency City",
        "facility_type": "Hospital",
        "icon": "hospital",
        "latitude": 12.9062,
        "longitude": 80.1983,
        "address": "Cheran Nagar, Perumbakkam / Medavakkam",
        "phone": "+91 44 4477 7000",
        "capacity": "350 Critical Care Beds",
        "icu_available": 50,
        "status": "Operational 24/7"
    },
    {
        "id": "loc_h11",
        "name": "Fortis Malar Emergency Care",
        "facility_type": "Hospital",
        "icon": "hospital",
        "latitude": 13.0041,
        "longitude": 80.2568,
        "address": "First Main Road, Gandhi Nagar, Adyar",
        "phone": "+91 44 4289 2222",
        "capacity": "160 Emergency Beds",
        "icu_available": 20,
        "status": "Operational 24/7"
    },
    {
        "id": "loc_h12",
        "name": "Sir Ivan Stedeford Emergency Hospital",
        "facility_type": "Hospital",
        "icon": "hospital",
        "latitude": 13.1180,
        "longitude": 80.1550,
        "address": "Ambattur OT, Ambattur",
        "phone": "+91 44 2658 0137",
        "capacity": "140 Emergency Beds",
        "icu_available": 18,
        "status": "Operational 24/7"
    },
    {
        "id": "loc_h13",
        "name": "Avadi Ordnance Emergency Medical Unit",
        "facility_type": "Hospital",
        "icon": "hospital",
        "latitude": 13.1250,
        "longitude": 80.0980,
        "address": "OFR Estate, Avadi",
        "phone": "+91 44 2638 2141",
        "capacity": "150 Emergency Beds",
        "icu_available": 22,
        "status": "Operational 24/7"
    },
    {
        "id": "loc_h14",
        "name": "Madhavaram Community Emergency Hospital",
        "facility_type": "Hospital",
        "icon": "hospital",
        "latitude": 13.1480,
        "longitude": 80.2310,
        "address": "GNT Road, Madhavaram",
        "phone": "+91 44 2553 0100",
        "capacity": "110 Emergency Beds",
        "icu_available": 12,
        "status": "Operational 24/7"
    },
    # Chennai Urban Community Health Centres (UCHC - Greater Chennai Corporation)
    {
        "id": "loc_uchc_1",
        "name": "Kuppam UCHC (Zone I, Div 11)",
        "facility_type": "Health Center",
        "uchc_zone": "I",
        "uchc_division": 11,
        "icon": "hospital",
        "latitude": 13.2185,
        "longitude": 80.3245,
        "address": "No.1, School Street, Jothy Nagar, Kuppam, Chennai - 600057",
        "phone": "044-25732100",
        "capacity": "50 Emergency Beds • 24/7 UCHC Primary Care",
        "icu_available": 6,
        "status": "Operational 24/7"
    },
    {
        "id": "loc_uchc_2",
        "name": "Manali UCHC (Zone II, Div 21)",
        "facility_type": "Health Center",
        "uchc_zone": "II",
        "uchc_division": 21,
        "icon": "hospital",
        "latitude": 13.1672,
        "longitude": 80.2618,
        "address": "No 1 Nedunchezian Salai, Manali, Chennai - 600068",
        "phone": "044-25941200",
        "capacity": "60 Emergency Beds • Trauma & Triage Center",
        "icu_available": 8,
        "status": "Operational 24/7"
    },
    {
        "id": "loc_uchc_3",
        "name": "Madhavaram UCHC (Zone III, Div 26)",
        "facility_type": "Health Center",
        "uchc_zone": "III",
        "uchc_division": 26,
        "icon": "hospital",
        "latitude": 13.1485,
        "longitude": 80.2312,
        "address": "No 47, Swamy Nagar, Madhavaram, Chennai - 600060",
        "phone": "044-25530122",
        "capacity": "55 Emergency Beds • 24/7 Ambulance Post",
        "icu_available": 6,
        "status": "Operational 24/7"
    },
    {
        "id": "loc_uchc_4",
        "name": "R.K. Nagar UCHC (Zone IV, Div 47)",
        "facility_type": "Health Center",
        "uchc_zone": "IV",
        "uchc_division": 47,
        "icon": "hospital",
        "latitude": 13.1162,
        "longitude": 80.2854,
        "address": "No.88, K.H Road, Korukkupet, Chennai - 600021",
        "phone": "044-25983411",
        "capacity": "70 Emergency Beds • Emergency Ward Active",
        "icu_available": 10,
        "status": "Operational 24/7"
    },
    {
        "id": "loc_uchc_5",
        "name": "Sanjeevarayanpet UCHC (Zone V, Div 49)",
        "facility_type": "Health Center",
        "uchc_zone": "V",
        "uchc_division": 49,
        "icon": "hospital",
        "latitude": 13.1092,
        "longitude": 80.2921,
        "address": "No.194, Solaiappar St, Old Washermanpet, Chennai - 600021",
        "phone": "044-25912300",
        "capacity": "65 Emergency Beds • Critical Stabilization Unit",
        "icu_available": 8,
        "status": "Operational 24/7"
    },
    {
        "id": "loc_uchc_6",
        "name": "Pulianthope UCHC (Zone VI, Div 73)",
        "facility_type": "Health Center",
        "uchc_zone": "VI",
        "uchc_division": 73,
        "icon": "hospital",
        "latitude": 13.0945,
        "longitude": 80.2682,
        "address": "42, Thiruvenkadasamy Street, Pulianthope, Chennai - 600012",
        "phone": "044-26671233",
        "capacity": "75 Emergency Beds • 24/7 Maternity & Trauma",
        "icu_available": 10,
        "status": "Operational 24/7"
    },
    {
        "id": "loc_uchc_7",
        "name": "Padi UCHC (Zone VII, Div 87)",
        "facility_type": "Health Center",
        "uchc_zone": "VII",
        "uchc_division": 87,
        "icon": "hospital",
        "latitude": 13.0974,
        "longitude": 80.1872,
        "address": "No. 5, Church St, TMP Nagar, Padi, Chennai - 600050",
        "phone": "044-26543100",
        "capacity": "60 Emergency Beds • Oxygen Supply Hub",
        "icu_available": 8,
        "status": "Operational 24/7"
    },
    {
        "id": "loc_uchc_8",
        "name": "Ayanavaram UCHC (Zone VIII, Div 96)",
        "facility_type": "Health Center",
        "uchc_zone": "VIII",
        "uchc_division": 96,
        "icon": "hospital",
        "latitude": 13.0961,
        "longitude": 80.2384,
        "address": "29, United India Nagar, Ayanavaram, Chennai - 600023",
        "phone": "044-26742311",
        "capacity": "70 Emergency Beds • 24/7 Critical Response",
        "icu_available": 10,
        "status": "Operational 24/7"
    },
    {
        "id": "loc_uchc_9",
        "name": "Mirsahibpet UCHC (Zone IX, Div 119)",
        "facility_type": "Health Center",
        "uchc_zone": "IX",
        "uchc_division": 119,
        "icon": "hospital",
        "latitude": 13.0564,
        "longitude": 80.2678,
        "address": "No.11, Begum 5th Street, Royapettah, Chennai - 600014",
        "phone": "044-28481299",
        "capacity": "80 Emergency Beds • Central Ward",
        "icu_available": 12,
        "status": "Operational 24/7"
    },
    {
        "id": "loc_uchc_10",
        "name": "Vadapalani UCHC (Zone X, Div 134)",
        "facility_type": "Health Center",
        "uchc_zone": "X",
        "uchc_division": 134,
        "icon": "hospital",
        "latitude": 13.0503,
        "longitude": 80.2132,
        "address": "No: 65, Arcot Road, Kodambakkam, Chennai - 600024",
        "phone": "044-24831200",
        "capacity": "85 Emergency Beds • Trauma & Pediatric Unit",
        "icu_available": 12,
        "status": "Operational 24/7"
    },
    {
        "id": "loc_uchc_11",
        "name": "Porur UCHC (Zone XI, Div 153)",
        "facility_type": "Health Center",
        "uchc_zone": "XI",
        "uchc_division": 153,
        "icon": "hospital",
        "latitude": 13.0384,
        "longitude": 80.1572,
        "address": "4, Senthil Nagar, Hospital Road, Chinna Porur, Chennai - 600116",
        "phone": "044-24761211",
        "capacity": "90 Emergency Beds • Flood Evacuation Ward",
        "icu_available": 15,
        "status": "Operational 24/7"
    },
    {
        "id": "loc_uchc_12",
        "name": "Alandur UCHC (Zone XII, Div 160)",
        "facility_type": "Health Center",
        "uchc_zone": "XII",
        "uchc_division": 160,
        "icon": "hospital",
        "latitude": 13.0031,
        "longitude": 80.2014,
        "address": "No.56, Sowri St, Alandur, Chennai - 600016",
        "phone": "044-22341200",
        "capacity": "75 Emergency Beds • Metro Corridor Medical Unit",
        "icu_available": 10,
        "status": "Operational 24/7"
    },
    {
        "id": "loc_uchc_13",
        "name": "Adyar UCHC (Zone XIII, Div 175)",
        "facility_type": "Health Center",
        "uchc_zone": "XIII",
        "uchc_division": 175,
        "icon": "hospital",
        "latitude": 13.0065,
        "longitude": 80.2573,
        "address": "No: 2, Venkatarathinam Nagar, Adyar, Chennai - 600020",
        "phone": "044-24411200",
        "capacity": "80 Emergency Beds • Coastal Response Team",
        "icu_available": 12,
        "status": "Operational 24/7"
    },
    {
        "id": "loc_uchc_14",
        "name": "Perungudi UCHC (Zone XIV, Div 184)",
        "facility_type": "Health Center",
        "uchc_zone": "XIV",
        "uchc_division": 184,
        "icon": "hospital",
        "latitude": 12.9642,
        "longitude": 80.2441,
        "address": "Next Division Office, School Road, Perungudi, Chennai - 600096",
        "phone": "044-24961200",
        "capacity": "70 Emergency Beds • OMR Emergency Hub",
        "icu_available": 10,
        "status": "Operational 24/7"
    },
    {
        "id": "loc_uchc_15",
        "name": "Kannagi Nagar UCHC (Zone XV, Div 195)",
        "facility_type": "Health Center",
        "uchc_zone": "XV",
        "uchc_division": 195,
        "icon": "hospital",
        "latitude": 12.9345,
        "longitude": 80.2305,
        "address": "Kannagi Nagar Slum Clearance Board, Kannagi Nagar, Chennai - 600115",
        "phone": "044-24581200",
        "capacity": "85 Emergency Beds • Community Emergency Center",
        "icu_available": 12,
        "status": "Operational 24/7"
    },
    {
        "id": "loc_uchc_16",
        "name": "Injambakkam UCHC (Zone XV, Div 196)",
        "facility_type": "Health Center",
        "uchc_zone": "XV",
        "uchc_division": 196,
        "icon": "hospital",
        "latitude": 12.9192,
        "longitude": 80.2524,
        "address": "VOC Street, Near Amma Unavagam, Injambakkam Peripheral Hospital, Chennai - 600115",
        "phone": "044-24491200",
        "capacity": "80 Emergency Beds • ECR Coastal Medical Station",
        "icu_available": 10,
        "status": "Operational 24/7"
    },
    # Relief Shelters & Evacuation Centers
    {
        "id": "loc_s1",
        "name": "Tambaram Indoor Stadium Relief Shelter",
        "facility_type": "Relief Shelter",
        "icon": "shelter",
        "latitude": 12.9200,
        "longitude": 80.1250,
        "address": "Gandhi Road, West Tambaram",
        "phone": "1800-425-1088",
        "capacity": "1,500 Evacuees",
        "food_water_status": "Abundant Supplies",
        "status": "Active Safe Zone"
    },
    {
        "id": "loc_s2",
        "name": "Central Community Disaster Shelter",
        "facility_type": "Relief Shelter",
        "icon": "shelter",
        "latitude": 13.0850,
        "longitude": 80.2650,
        "address": "Ripon Building Complex, Central",
        "phone": "1800-425-1089",
        "capacity": "3,000 Evacuees",
        "food_water_status": "Abundant Supplies",
        "status": "Active Safe Zone"
    },
    {
        "id": "loc_s3",
        "name": "North Harbor Coastal Evacuation Base",
        "facility_type": "Relief Shelter",
        "icon": "shelter",
        "latitude": 13.1250,
        "longitude": 80.2950,
        "address": "Harbor High School Grounds",
        "phone": "1800-425-1090",
        "capacity": "2,000 Evacuees",
        "food_water_status": "Stocked",
        "status": "Active Safe Zone"
    },
    {
        "id": "loc_s4",
        "name": "Western Basin Disaster Relief Camp",
        "facility_type": "Relief Shelter",
        "icon": "shelter",
        "latitude": 13.0550,
        "longitude": 80.1750,
        "address": "Punamallee High Road Assembly Hub",
        "phone": "1800-425-1091",
        "capacity": "1,200 Evacuees",
        "food_water_status": "Stocked",
        "status": "Active Safe Zone"
    },
    # Fire & Police First Responder Bases
    {
        "id": "loc_f1",
        "name": "Tambaram Fire & Heavy Rescue Station",
        "facility_type": "Fire Station",
        "icon": "fire",
        "latitude": 12.9260,
        "longitude": 80.1310,
        "address": "GST Road, Tambaram East",
        "phone": "101",
        "capacity": "6 Rescue Engines",
        "status": "High Alert"
    },
    {
        "id": "loc_f2",
        "name": "Central Heavy Fire & Hazmat Station",
        "facility_type": "Fire Station",
        "icon": "fire",
        "latitude": 13.0800,
        "longitude": 80.2720,
        "address": "High Court Compound, Central",
        "phone": "101",
        "capacity": "10 Rescue Engines",
        "status": "High Alert"
    },
    {
        "id": "loc_p1",
        "name": "Tambaram Police Command & Evacuation Control",
        "facility_type": "Police Hub",
        "icon": "police",
        "latitude": 12.9210,
        "longitude": 80.1280,
        "address": "MUD Complex, Tambaram",
        "phone": "100",
        "capacity": "Command Squads Active",
        "status": "24/7 Command Patrol"
    },
    {"id": "fire001", "name": "Secunderabad", "facility_type": "Fire Station", "icon": "fire", "latitude": 17.3322, "longitude": 78.4157, "address": "Secunderabad, Hyderabad, Telangana", "phone": "8712699428", "capacity": "5 Rescue Engines", "status": "Operational 24/7"},
    {"id": "fire002", "name": "Snorkel", "facility_type": "Fire Station", "icon": "fire", "latitude": 17.409, "longitude": 78.4844, "address": "Secunderabad area, Hyderabad, Telangana", "phone": "8712699432", "capacity": "5 Rescue Engines", "status": "Operational 24/7"},
    {"id": "fire003", "name": "Musheerabad", "facility_type": "Fire Station", "icon": "fire", "latitude": 17.4342, "longitude": 78.5807, "address": "Musheerabad, Hyderabad, Telangana", "phone": "8712699426", "capacity": "5 Rescue Engines", "status": "Operational 24/7"},
    {"id": "fire004", "name": "Sanathnagar", "facility_type": "Fire Station", "icon": "fire", "latitude": 17.4445, "longitude": 78.3923, "address": "Sanath Nagar, Hyderabad, Telangana", "phone": "8712699430", "capacity": "5 Rescue Engines", "status": "Operational 24/7"},
    {"id": "fire005", "name": "Gowliguda", "facility_type": "Fire Station", "icon": "fire", "latitude": 17.3113, "longitude": 78.4383, "address": "Gowliguda, Hyderabad, Telangana", "phone": "8712699410", "capacity": "5 Rescue Engines", "status": "Operational 24/7"},
    {"id": "fire006", "name": "Malakpet", "facility_type": "Fire Station", "icon": "fire", "latitude": 17.4573, "longitude": 78.5572, "address": "Malakpet, Hyderabad, Telangana", "phone": "8712699414", "capacity": "5 Rescue Engines", "status": "Operational 24/7"},
    {"id": "fire007", "name": "Chandulal Baradari", "facility_type": "Fire Station", "icon": "fire", "latitude": 17.3986, "longitude": 78.5233, "address": "Chandulal Baradari, Hyderabad, Telangana", "phone": "8712699412", "capacity": "5 Rescue Engines", "status": "Operational 24/7"},
    {"id": "fire008", "name": "Moghalpura", "facility_type": "Fire Station", "icon": "fire", "latitude": 17.3701, "longitude": 78.4682, "address": "Moghalpura, Hyderabad, Telangana", "phone": "8712699408", "capacity": "5 Rescue Engines", "status": "Operational 24/7"},
    {"id": "fire009", "name": "High Court", "facility_type": "Fire Station", "icon": "fire", "latitude": 17.3675, "longitude": 78.4506, "address": "High Court area, Hyderabad, Telangana", "phone": "8712699418", "capacity": "5 Rescue Engines", "status": "Operational 24/7"},
    {"id": "fire010", "name": "Salarjung Museum", "facility_type": "Fire Station", "icon": "fire", "latitude": 17.3487, "longitude": 78.5205, "address": "Salarjung Museum area, Hyderabad, Telangana", "phone": "8712699416", "capacity": "5 Rescue Engines", "status": "Operational 24/7"},
    {"id": "fire011", "name": "Langer House", "facility_type": "Fire Station", "icon": "fire", "latitude": 17.4485, "longitude": 78.4902, "address": "Langer House, Hyderabad, Telangana", "phone": "8712699420", "capacity": "5 Rescue Engines", "status": "Operational 24/7"},
    {"id": "fire012", "name": "Panjagutta", "facility_type": "Fire Station", "icon": "fire", "latitude": 17.3772, "longitude": 78.4583, "address": "Panjagutta, Hyderabad, Telangana", "phone": "8712699424", "capacity": "5 Rescue Engines", "status": "Operational 24/7"},
    {"id": "fire013", "name": "Turn Table Ladder", "facility_type": "Fire Station", "icon": "fire", "latitude": 17.3468, "longitude": 78.465, "address": "Hyderabad, Telangana; specialist ladder unit location to confirm", "phone": "8712699438", "capacity": "5 Rescue Engines", "status": "Operational 24/7"},
    {"id": "fire014", "name": "Secretariat-2", "facility_type": "Fire Station", "icon": "fire", "latitude": 17.3866, "longitude": 78.4392, "address": "Secretariat area, Hyderabad, Telangana", "phone": "8712699440", "capacity": "5 Rescue Engines", "status": "Operational 24/7"},
    {"id": "fire015", "name": "Secretariat-1", "facility_type": "Fire Station", "icon": "fire", "latitude": 17.3124, "longitude": 78.4782, "address": "Secretariat area, Hyderabad, Telangana", "phone": "8712699440", "capacity": "5 Rescue Engines", "status": "Operational 24/7"},
    {"id": "fire016", "name": "Secretariat-3", "facility_type": "Fire Station", "icon": "fire", "latitude": 17.4173, "longitude": 78.5796, "address": "Secretariat area, Hyderabad, Telangana", "phone": "8712699440", "capacity": "5 Rescue Engines", "status": "Operational 24/7"},
    {"id": "fire017", "name": "Assembly-2", "facility_type": "Fire Station", "icon": "fire", "latitude": 17.4461, "longitude": 78.3897, "address": "Legislative Assembly area, Hyderabad, Telangana", "phone": "8712699464", "capacity": "5 Rescue Engines", "status": "Operational 24/7"},
    {"id": "fire018", "name": "Legislative Assembly", "facility_type": "Fire Station", "icon": "fire", "latitude": 17.4818, "longitude": 78.4772, "address": "Legislative Assembly area, Hyderabad, Telangana", "phone": "8712699442", "capacity": "5 Rescue Engines", "status": "Operational 24/7"},
    {"id": "fire019", "name": "Assembly-1", "facility_type": "Fire Station", "icon": "fire", "latitude": 17.4732, "longitude": 78.5844, "address": "Legislative Assembly area, Hyderabad, Telangana", "phone": "8712699450", "capacity": "5 Rescue Engines", "status": "Operational 24/7"},
    {"id": "fire020", "name": "Moulali", "facility_type": "Fire Station", "icon": "fire", "latitude": 17.3296, "longitude": 78.5733, "address": "Moulali, Hyderabad, Telangana", "phone": "8712699434", "capacity": "5 Rescue Engines", "status": "Operational 24/7"},
    {"id": "fire021", "name": "Secunderabad Cantonment", "facility_type": "Fire Station", "icon": "fire", "latitude": 17.3872, "longitude": 78.5417, "address": "Secunderabad Cantonment, Telangana", "phone": "8712699436", "capacity": "5 Rescue Engines", "status": "Operational 24/7"},
    {"id": "fire022", "name": "Hayathnagar", "facility_type": "Fire Station", "icon": "fire", "latitude": 17.3258, "longitude": 78.4603, "address": "Hayathnagar, Ranga Reddy district, Telangana", "phone": "8712699406", "capacity": "5 Rescue Engines", "status": "Operational 24/7"},
    {"id": "fire023", "name": "Maheshwaram", "facility_type": "Fire Station", "icon": "fire", "latitude": 17.3772, "longitude": 78.5357, "address": "Maheshwaram, Ranga Reddy district, Telangana", "phone": "8712699456", "capacity": "5 Rescue Engines", "status": "Operational 24/7"},
    {"id": "fire024", "name": "Ibrahimpatnam", "facility_type": "Fire Station", "icon": "fire", "latitude": 17.3128, "longitude": 78.4783, "address": "Ibrahimpatnam, Ranga Reddy district, Telangana", "phone": "8712699458", "capacity": "5 Rescue Engines", "status": "Operational 24/7"},
    {"id": "fire025", "name": "Malkajgiri", "facility_type": "Fire Station", "icon": "fire", "latitude": 17.2912, "longitude": 78.4381, "address": "Malkajgiri, Telangana", "phone": "8712699402", "capacity": "5 Rescue Engines", "status": "Operational 24/7"},
    {"id": "fire026", "name": "Madhapur", "facility_type": "Fire Station", "icon": "fire", "latitude": 17.3468, "longitude": 78.4398, "address": "Madhapur, Hyderabad metro area, Telangana", "phone": "8712699446", "capacity": "5 Rescue Engines", "status": "Operational 24/7"},
    {"id": "fire027", "name": "Bronto Sky Lift, Madhapur", "facility_type": "Fire Station", "icon": "fire", "latitude": 17.4716, "longitude": 78.4148, "address": "Madhapur, Hyderabad, Telangana; specialist vehicle unit", "phone": "8712699454", "capacity": "5 Rescue Engines", "status": "Operational 24/7"},
    {"id": "fire028", "name": "Kukatpally", "facility_type": "Fire Station", "icon": "fire", "latitude": 17.4695, "longitude": 78.5589, "address": "Kukatpally, Hyderabad metro area, Telangana", "phone": "8712699394", "capacity": "5 Rescue Engines", "status": "Operational 24/7"},
    {"id": "fire029", "name": "Hazmat Vehicle, Kukatpally", "facility_type": "Fire Station", "icon": "fire", "latitude": 17.3688, "longitude": 78.4629, "address": "Kukatpally, Hyderabad metro area, Telangana; specialist unit", "phone": "8712699400", "capacity": "5 Rescue Engines", "status": "Operational 24/7"},
    {"id": "fire030", "name": "Chevella", "facility_type": "Fire Station", "icon": "fire", "latitude": 17.4677, "longitude": 78.5306, "address": "Chevella, Ranga Reddy district, Telangana", "phone": "8712699452", "capacity": "5 Rescue Engines", "status": "Operational 24/7"},
    {"id": "fire031", "name": "Yakutpura", "facility_type": "Fire Station", "icon": "fire", "latitude": 17.37, "longitude": 78.4205, "address": "Yakutpura, Hyderabad, Telangana", "phone": "8712699423", "capacity": "5 Rescue Engines", "status": "Operational 24/7"},
    {"id": "fire032", "name": "Rajendranagar-1", "facility_type": "Fire Station", "icon": "fire", "latitude": 17.4146, "longitude": 78.4775, "address": "Rajendranagar, Ranga Reddy district, Telangana", "phone": "8712699460", "capacity": "5 Rescue Engines", "status": "Operational 24/7"},
    {"id": "fire033", "name": "LB Nagar-2", "facility_type": "Fire Station", "icon": "fire", "latitude": 17.3878, "longitude": 78.3928, "address": "LB Nagar, Hyderabad metro area, Telangana", "phone": "8712685790", "capacity": "5 Rescue Engines", "status": "Operational 24/7"},
    {"id": "fire034", "name": "Amberpet-1", "facility_type": "Fire Station", "icon": "fire", "latitude": 17.3113, "longitude": 78.4137, "address": "Amberpet, Hyderabad, Telangana", "phone": "8712695358", "capacity": "5 Rescue Engines", "status": "Operational 24/7"},
    {"id": "fire035", "name": "Amberpet-2", "facility_type": "Fire Station", "icon": "fire", "latitude": 17.3792, "longitude": 78.478, "address": "Amberpet, Hyderabad, Telangana", "phone": "8712695358", "capacity": "5 Rescue Engines", "status": "Operational 24/7"},
    {"id": "hosp001", "name": "Osmania General Hospital", "facility_type": "Hospital", "icon": "hospital", "latitude": 17.2991, "longitude": 78.4479, "address": "15-6-103, Afzalgunj Road, Hyderabad, Telangana 500012", "phone": "040-23538846; 040-24600146", "capacity": "150 Emergency Beds", "status": "Operational 24/7", "icu_available": 38},
    {"id": "hosp002", "name": "Gandhi Hospital", "facility_type": "Hospital", "icon": "hospital", "latitude": 17.2891, "longitude": 78.3903, "address": "Musheerabad, Padmarao Nagar, Secunderabad, Telangana 500003", "phone": "040-27505566", "capacity": "150 Emergency Beds", "status": "Operational 24/7", "icu_available": 45},
    {"id": "hosp003", "name": "Government Chest Hospital", "facility_type": "Hospital", "icon": "hospital", "latitude": 17.3773, "longitude": 78.4326, "address": "Erragadda area, Hyderabad, Telangana; exact entrance address to confirm", "phone": "040-23814421; 040-23814422; 040-23814423; 040-23814424", "capacity": "150 Emergency Beds", "status": "Operational 24/7", "icu_available": 43},
    {"id": "hosp004", "name": "Government ENT Hospital", "facility_type": "Hospital", "icon": "hospital", "latitude": 17.338, "longitude": 78.4655, "address": "Koti area, Hyderabad, Telangana; exact entrance address to confirm", "phone": "040-24740245; 040-24742329", "capacity": "150 Emergency Beds", "status": "Operational 24/7", "icu_available": 46},
    {"id": "hosp005", "name": "Apollo Hospitals, Jubilee Hills", "facility_type": "Hospital", "icon": "hospital", "latitude": 17.4657, "longitude": 78.5542, "address": "Road No. 72, opposite Bharatiya Vidya Bhavan School, Film Nagar, Jubilee Hills, Hyderabad 500096", "phone": "+91 40 6907 1200", "capacity": "150 Emergency Beds", "status": "Operational 24/7", "icu_available": 20},
    {"id": "hosp006", "name": "Yashoda Hospitals, Somajiguda", "facility_type": "Hospital", "icon": "hospital", "latitude": 17.4683, "longitude": 78.5265, "address": "6-3-905, Raj Bhavan Road, Somajiguda, Hyderabad 500082", "phone": "+91 40 6723 2348", "capacity": "150 Emergency Beds", "status": "Operational 24/7", "icu_available": 18},
    {"id": "hosp007", "name": "Medicover Hospitals, HITEC City", "facility_type": "Hospital", "icon": "hospital", "latitude": 17.3584, "longitude": 78.5487, "address": "HUDA Techno Enclave, behind Cyber Towers, HITEC City, Hyderabad 500081", "phone": "+91 40 6833 4455", "capacity": "150 Emergency Beds", "status": "Operational 24/7", "icu_available": 15},
    {"id": "hosp008", "name": "Aster Prime Hospital", "facility_type": "Hospital", "icon": "hospital", "latitude": 17.3486, "longitude": 78.4954, "address": "Plot No. 4, HMDA Maitrivanam, Satyam Theatre Road, Ameerpet, Hyderabad 500038", "phone": "+91 40 4959 4959", "capacity": "150 Emergency Beds", "status": "Operational 24/7", "icu_available": 35},
    {"id": "fire036", "name": "Fire Station, Film Nagar", "facility_type": "Fire Station", "icon": "fire", "latitude": 17.4154, "longitude": 78.3891, "address": "Road No. 7, Durga Bhawani Nagar, MRC Colony, Jubilee Hills, Hyderabad 500096", "phone": "+91 40 2344 2953", "capacity": "5 Rescue Engines", "status": "Operational 24/7"},
    {"id": "fire037", "name": "Fire Station, Sanath Nagar", "facility_type": "Fire Station", "icon": "fire", "latitude": 17.3911, "longitude": 78.4414, "address": "Sanath Nagar Main Road, Sanath Nagar, Hyderabad 500018", "phone": "8712699430", "capacity": "5 Rescue Engines", "status": "Operational 24/7"},
    {"id": "resp001", "name": "Telangana Ambulance Emergency Service", "facility_type": "Ambulance Hub", "icon": "ambulance", "latitude": 17.4746, "longitude": 78.4693, "address": "Statewide dispatch; exact local ambulance base depends on incident", "phone": "108", "capacity": "10 Ambulances", "status": "Operational 24/7"},
    {"id": "resp002", "name": "Ambulance Helpline", "facility_type": "Ambulance Hub", "icon": "ambulance", "latitude": 17.4427, "longitude": 78.5112, "address": "Statewide helpline; local service coverage to be confirmed", "phone": "102", "capacity": "10 Ambulances", "status": "Operational 24/7"},
    {"id": "resp003", "name": "Integrated Emergency Response Support System", "facility_type": "Relief Shelter", "icon": "shelter", "latitude": 17.4278, "longitude": 78.5836, "address": "Statewide emergency dispatch", "phone": "112", "capacity": "Unknown Capacity", "status": "Operational 24/7"},
    {"id": "resp004", "name": "Fire and Rescue Emergency Helpline", "facility_type": "Fire Station", "icon": "fire", "latitude": 17.4178, "longitude": 78.5156, "address": "Statewide emergency dispatch", "phone": "101", "capacity": "5 Rescue Engines", "status": "Operational 24/7"},
    {"id": "resp005", "name": "Disaster Helpline", "facility_type": "Control Room", "icon": "police", "latitude": 17.4025, "longitude": 78.43, "address": "Hyderabad district control / disaster response", "phone": "1077", "capacity": "Command Center", "status": "Operational 24/7"},
    {"id": "resp006", "name": "State Control Room", "facility_type": "Control Room", "icon": "police", "latitude": 17.4655, "longitude": 78.4669, "address": "Telangana state control room", "phone": "1070", "capacity": "Command Center", "status": "Operational 24/7"}
,
    {"id": "hosp009", "name": "District Hospital King Koti", "facility_type": "Hospital", "icon": "hospital", "latitude": 17.3525, "longitude": 78.4461, "address": "King Koti / Hyderguda, Hyderabad, Telangana 500001", "phone": "Unknown", "capacity": "150 Emergency Beds", "status": "Operational 24/7", "icu_available": 48},
    {"id": "hosp010", "name": "Area Hospital Nampally", "facility_type": "Hospital", "icon": "hospital", "latitude": 17.2873, "longitude": 78.4077, "address": "Nampally, Hyderabad, Telangana", "phone": "Unknown", "capacity": "150 Emergency Beds", "status": "Operational 24/7", "icu_available": 17},
    {"id": "hosp011", "name": "Area Hospital Malakpet", "facility_type": "Hospital", "icon": "hospital", "latitude": 17.4381, "longitude": 78.4675, "address": "Malakpet, Hyderabad, Telangana", "phone": "Unknown", "capacity": "150 Emergency Beds", "status": "Operational 24/7", "icu_available": 17},
    {"id": "hosp012", "name": "Area Hospital Golconda", "facility_type": "Hospital", "icon": "hospital", "latitude": 17.4451, "longitude": 78.5651, "address": "Golconda, Hyderabad, Telangana", "phone": "Unknown", "capacity": "150 Emergency Beds", "status": "Operational 24/7", "icu_available": 16},
    {"id": "hosp013", "name": "Area Hospital Kamatipura", "facility_type": "Hospital", "icon": "hospital", "latitude": 17.4669, "longitude": 78.4195, "address": "Kamatipura, Hyderabad, Telangana", "phone": "Unknown", "capacity": "150 Emergency Beds", "status": "Operational 24/7", "icu_available": 30},
    {"id": "hosp014", "name": "Area Hospital Bandlaguda", "facility_type": "Hospital", "icon": "hospital", "latitude": 17.3425, "longitude": 78.4882, "address": "Bandlaguda, Hyderabad, Telangana", "phone": "Unknown", "capacity": "150 Emergency Beds", "status": "Operational 24/7", "icu_available": 30},
    {"id": "hosp015", "name": "Area Hospital Dabeerpura", "facility_type": "Hospital", "icon": "hospital", "latitude": 17.4491, "longitude": 78.4068, "address": "Dabeerpura, Hyderabad, Telangana", "phone": "Unknown", "capacity": "150 Emergency Beds", "status": "Operational 24/7", "icu_available": 12},
    {"id": "hosp016", "name": "District Hospital Tandur", "facility_type": "Hospital", "icon": "hospital", "latitude": 17.3623, "longitude": 78.5373, "address": "Tandur, Vikarabad district, Telangana", "phone": "Unknown", "capacity": "150 Emergency Beds", "status": "Operational 24/7", "icu_available": 33},
    {"id": "hosp017", "name": "District Hospital Sangareddy", "facility_type": "Hospital", "icon": "hospital", "latitude": 17.4514, "longitude": 78.547, "address": "Sangareddy, Telangana", "phone": "Unknown", "capacity": "150 Emergency Beds", "status": "Operational 24/7", "icu_available": 13},
    {"id": "hosp018", "name": "Government Area Hospital, Gachibowli/Kondapur", "facility_type": "Hospital", "icon": "hospital", "latitude": 17.4026, "longitude": 78.4082, "address": "Kondapur Main Road, Masjid Banda, Gachibowli, Hyderabad 500084", "phone": "Unknown", "capacity": "150 Emergency Beds", "status": "Operational 24/7", "icu_available": 22},
    {"id": "hosp019", "name": "KIMS-Sunshine Hospitals, Begumpet", "facility_type": "Hospital", "icon": "hospital", "latitude": 17.3535, "longitude": 78.5137, "address": "Metro Pillar C1327, beside Jamia Masjid, Prakash Nagar, Begumpet, Hyderabad 500003", "phone": "+91 40 4455 0000", "capacity": "150 Emergency Beds", "status": "Operational 24/7", "icu_available": 27},
    {"id": "hosp020", "name": "District Hospital King Koti (map listing)", "facility_type": "Hospital", "icon": "hospital", "latitude": 17.2994, "longitude": 78.5296, "address": "3-5-773, Hyderguda, King Koti Road, Hyderabad 500001", "phone": "+91 80085 553878", "capacity": "150 Emergency Beds", "status": "Operational 24/7", "icu_available": 29},
    {"id": "hosp021", "name": "Government General and Chest Hospital, Erragadda", "facility_type": "Hospital", "icon": "hospital", "latitude": 17.3611, "longitude": 78.523, "address": "Kalyan Nagar Phase 1, Sunder Nagar, Hyderabad 500038", "phone": "Unknown", "capacity": "150 Emergency Beds", "status": "Operational 24/7", "icu_available": 23},
    {"id": "hosp022", "name": "Apollo Hospitals, Secunderabad", "facility_type": "Hospital", "icon": "hospital", "latitude": 17.4416, "longitude": 78.5666, "address": "Secunderabad, Telangana; exact facility address to verify", "phone": "Unknown", "capacity": "150 Emergency Beds", "status": "Operational 24/7", "icu_available": 14},
    {"id": "hosp023", "name": "Continental Hospitals", "facility_type": "Hospital", "icon": "hospital", "latitude": 17.3141, "longitude": 78.521, "address": "Nanakramguda, Financial District, Hyderabad, Telangana", "phone": "Unknown", "capacity": "150 Emergency Beds", "status": "Operational 24/7", "icu_available": 41},
    {"id": "hosp024", "name": "CARE Hospitals, HITEC City", "facility_type": "Hospital", "icon": "hospital", "latitude": 17.4652, "longitude": 78.5465, "address": "HITEC City / Madhapur area, Hyderabad, Telangana", "phone": "Unknown", "capacity": "150 Emergency Beds", "status": "Operational 24/7", "icu_available": 29},
    {"id": "fire038", "name": "Jeedimetla Fire Station", "facility_type": "Fire Station", "icon": "fire", "latitude": 17.4272, "longitude": 78.4029, "address": "Jeedimetla, Hyderabad metro area, Telangana", "phone": "Unknown", "capacity": "5 Rescue Engines", "status": "Operational 24/7"},
    {"id": "fire039", "name": "Model Fire Station, Gachibowli", "facility_type": "Fire Station", "icon": "fire", "latitude": 17.464, "longitude": 78.4398, "address": "Gachibowli, Hyderabad, Telangana", "phone": "Unknown", "capacity": "5 Rescue Engines", "status": "Operational 24/7"},
    {"id": "fire040", "name": "Cherrapally Fire Station", "facility_type": "Fire Station", "icon": "fire", "latitude": 17.4816, "longitude": 78.3928, "address": "Cherlapally / Cherrapally area, Telangana", "phone": "Unknown", "capacity": "5 Rescue Engines", "status": "Operational 24/7"},
    {"id": "fire041", "name": "Genome Valley Fire Station", "facility_type": "Fire Station", "icon": "fire", "latitude": 17.462, "longitude": 78.4503, "address": "Shameerpet / Genome Valley, Telangana", "phone": "Unknown", "capacity": "5 Rescue Engines", "status": "Operational 24/7"},
    {"id": "fire042", "name": "Shadnagar Fire Station", "facility_type": "Fire Station", "icon": "fire", "latitude": 17.4244, "longitude": 78.4103, "address": "Shadnagar, Rangareddy district, Telangana", "phone": "Unknown", "capacity": "5 Rescue Engines", "status": "Operational 24/7"},
    {"id": "fire043", "name": "Pargi Fire Station", "facility_type": "Fire Station", "icon": "fire", "latitude": 17.3844, "longitude": 78.5792, "address": "Pargi, Vikarabad district, Telangana", "phone": "Unknown", "capacity": "5 Rescue Engines", "status": "Operational 24/7"},
    {"id": "fire044", "name": "Tandur Fire Station", "facility_type": "Fire Station", "icon": "fire", "latitude": 17.3474, "longitude": 78.4367, "address": "Tandur, Vikarabad district, Telangana", "phone": "Unknown", "capacity": "5 Rescue Engines", "status": "Operational 24/7"},
    {"id": "fire045", "name": "Vikarabad Fire Station", "facility_type": "Fire Station", "icon": "fire", "latitude": 17.3744, "longitude": 78.5652, "address": "Vikarabad, Telangana", "phone": "Unknown", "capacity": "5 Rescue Engines", "status": "Operational 24/7"},
    {"id": "fire046", "name": "Kodangal Fire Station", "facility_type": "Fire Station", "icon": "fire", "latitude": 17.4399, "longitude": 78.4758, "address": "Kodangal, Vikarabad district, Telangana", "phone": "Unknown", "capacity": "5 Rescue Engines", "status": "Operational 24/7"},
    {"id": "fire047", "name": "Bhongir Fire Station", "facility_type": "Fire Station", "icon": "fire", "latitude": 17.3315, "longitude": 78.4778, "address": "Bhongir, Yadadri Bhuvanagiri district, Telangana", "phone": "Unknown", "capacity": "5 Rescue Engines", "status": "Operational 24/7"},
    {"id": "fire048", "name": "Yadagirigutta Fire Station", "facility_type": "Fire Station", "icon": "fire", "latitude": 17.2919, "longitude": 78.444, "address": "Yadagirigutta, Yadadri Bhuvanagiri district, Telangana", "phone": "Unknown", "capacity": "5 Rescue Engines", "status": "Operational 24/7"},
    {"id": "fire049", "name": "Choutuppal Fire Station", "facility_type": "Fire Station", "icon": "fire", "latitude": 17.3938, "longitude": 78.4786, "address": "Choutuppal, Yadadri Bhuvanagiri district, Telangana", "phone": "Unknown", "capacity": "5 Rescue Engines", "status": "Operational 24/7"},
    {"id": "fire050", "name": "Sangareddy Fire Station", "facility_type": "Fire Station", "icon": "fire", "latitude": 17.3661, "longitude": 78.4499, "address": "Sangareddy, Telangana", "phone": "Unknown", "capacity": "5 Rescue Engines", "status": "Operational 24/7"},
    {"id": "fire051", "name": "Patancheru Fire Station", "facility_type": "Fire Station", "icon": "fire", "latitude": 17.3667, "longitude": 78.5207, "address": "Patancheru, Sangareddy district, Telangana", "phone": "Unknown", "capacity": "5 Rescue Engines", "status": "Operational 24/7"},
    {"id": "fire052", "name": "Shamirpet Fire Station", "facility_type": "Fire Station", "icon": "fire", "latitude": 17.4439, "longitude": 78.554, "address": "Shamirpet, Medchal-Malkajgiri district, Telangana", "phone": "Unknown", "capacity": "5 Rescue Engines", "status": "Operational 24/7"},
    {"id": "fire053", "name": "Rajendranagar Fire Station", "facility_type": "Fire Station", "icon": "fire", "latitude": 17.34, "longitude": 78.4913, "address": "Rajendranagar, Rangareddy district, Telangana", "phone": "Unknown", "capacity": "5 Rescue Engines", "status": "Operational 24/7"},
    {"id": "fire054", "name": "Ibrahimpatnam Fire Station", "facility_type": "Fire Station", "icon": "fire", "latitude": 17.2954, "longitude": 78.5551, "address": "Ibrahimpatnam, Rangareddy district, Telangana", "phone": "Unknown", "capacity": "5 Rescue Engines", "status": "Operational 24/7"},
    {"id": "fire055", "name": "Maheshwaram Fire Station", "facility_type": "Fire Station", "icon": "fire", "latitude": 17.3387, "longitude": 78.4909, "address": "Maheshwaram, Rangareddy district, Telangana", "phone": "Unknown", "capacity": "5 Rescue Engines", "status": "Operational 24/7"},
    {"id": "fire056", "name": "Chevella Fire Station", "facility_type": "Fire Station", "icon": "fire", "latitude": 17.2984, "longitude": 78.5745, "address": "Chevella, Rangareddy district, Telangana", "phone": "Unknown", "capacity": "5 Rescue Engines", "status": "Operational 24/7"},
    {"id": "resp007", "name": "digniMuv Ambulance Service", "facility_type": "Ambulance Hub", "icon": "ambulance", "latitude": 17.473, "longitude": 78.5032, "address": "2nd Floor, Prasad Hospitals, Marrichettu Road, Manikonda, Hyderabad 500089", "phone": "+91 91007 10000", "capacity": "10 Ambulances", "status": "Operational 24/7"},
    {"id": "resp008", "name": "Ambulance Service, Banjara Hills/Somajiguda", "facility_type": "Ambulance Hub", "icon": "ambulance", "latitude": 17.3129, "longitude": 78.4401, "address": "Matha Nagar, Banjara Hills/Somajiguda area, Hyderabad 500082", "phone": "+91 99485 82750", "capacity": "10 Ambulances", "status": "Operational 24/7"}

]


# Database Access Interface
class LocalDatabaseStore:
    def __init__(self):
        self.disasters = list(INITIAL_DISASTERS)
        self.affected_areas = list(INITIAL_AREAS)
        self.resources = list(INITIAL_RESOURCES)
        self.resource_requests = list(INITIAL_REQUESTS)
        self.rescue_teams = list(INITIAL_TEAMS)
        self.vehicles = list(INITIAL_VEHICLES)
        self.alerts = list(INITIAL_ALERTS)
        self.disaster_reports = list(INITIAL_REPORTS)
        self.safe_locations = list(INITIAL_SAFE_LOCATIONS)
        self.allocations = []

db_store = LocalDatabaseStore()
