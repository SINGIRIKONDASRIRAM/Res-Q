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

# Hyderabad & Telangana Emergency Dataset Integration
from services.emergency_dataset_loader import (
    load_healthcare_resources,
    load_emergency_response_teams,
    load_sample_incidents,
    format_facilities_for_safe_locations,
    load_telangana_safe_locations
)

INITIAL_HEALTHCARE_RESOURCES = load_healthcare_resources()
INITIAL_RESPONSE_TEAMS = load_emergency_response_teams()
INITIAL_SAMPLE_INCIDENTS = load_sample_incidents()

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
    {"id": "req10", "area_id": "a1", "area_name": "Area A - Coastal Sector 1", "resource_type": "Oxygen Cylinders", "quantity": 20, "urgency": "Critical", "description": "Emergency ICU ward setup at field hospital.", "status": "Approved", "created_at": "2026-08-13T15:00:00Z"},
    # Telangana & Hyderabad Demo Incident Allocations
    {"id": "req_hyd_001", "area_id": "area_hyd_101", "area_name": "Hitec City IT Corridor", "resource_type": "Ambulance", "quantity": 2, "urgency": "High", "description": "Road accident at Cyber Towers junction. 3 people affected. Dispatched 108 Ambulance.", "status": "Approved", "created_at": "2026-10-16T22:15:00Z"},
    {"id": "req_hyd_002", "area_id": "area_hyd_102", "area_name": "Gachibowli Financial District", "resource_type": "Rescue Teams", "quantity": 2, "urgency": "High", "description": "Urban inundation in residential lowlands. 12 people stranded. Assigned to HYDRAA DRF.", "status": "Approved", "created_at": "2026-10-16T22:18:00Z"},
    {"id": "req_hyd_003", "area_id": "area_hyd_101", "area_name": "Secunderabad Railway Station", "resource_type": "First Aid Kits", "quantity": 25, "urgency": "Critical", "description": "Commercial fire incident near railway hub. 5 casualties reported. Assigned to Telangana Fire 101 & Gandhi Hospital.", "status": "Approved", "created_at": "2026-10-16T22:20:00Z"}
]

INITIAL_TEAMS = [
    {"id": "t1", "team_name": "Alpha Medical ResQ-1", "leader": "Dr. Aris Thorne", "members": 8, "specialization": "Medical", "location": "Coastal Sector 1", "status": "On Mission", "assigned_area_id": "a1", "assigned_area_name": "Area A - Coastal Sector 1"},
    {"id": "t2", "team_name": "Bravo NDRF Battalion 4", "leader": "Capt. Rajesh Kumar", "members": 15, "specialization": "Search & Rescue", "location": "Riverbed Township", "status": "Assigned", "assigned_area_id": "a3", "assigned_area_name": "Area C - Riverbed Township"},
    {"id": "t3", "team_name": "Charlie Coast Guard Squad", "leader": "Cmdr. Vikram Sethi", "members": 12, "specialization": "Evacuation", "location": "Fisherman Island", "status": "On Mission", "assigned_area_id": "a5", "assigned_area_name": "Area E - Fisherman Island"},
    {"id": "t4", "team_name": "Delta Hazmat Response", "leader": "Lt. Maya Lin", "members": 6, "specialization": "Hazmat", "location": "Central Depot", "status": "Available", "assigned_area_id": None, "assigned_area_name": None},
    {"id": "t5", "team_name": "Echo General Relief Contingent", "leader": "Sgt. David Miller", "members": 20, "specialization": "General Relief", "location": "North Harbor", "status": "Available", "assigned_area_id": None, "assigned_area_name": None},
    # Telangana Official Emergency Teams & Helplines (emergency_response_teams.csv)
    {"id": "t_hyd_108", "team_name": "Telangana 108 Ambulance Dispatch Unit 1", "leader": "Coord. Ramesh V", "members": 4, "specialization": "Medical", "location": "Hitec City Fleet Base", "status": "Available", "assigned_area_id": "area_hyd_101", "assigned_area_name": "Hitec City IT Corridor", "contact_number": "108"},
    {"id": "t_hydraa_drf", "team_name": "HYDRAA Disaster Response Force (DRF)", "leader": "Cmdr. AV Ranganath", "members": 24, "specialization": "Search & Rescue", "location": "GHMC Central Disaster Base", "status": "Available", "assigned_area_id": None, "assigned_area_name": None, "contact_number": "9000113667"},
    {"id": "t_hyd_fire", "team_name": "Telangana Fire & Heavy Rescue Squad", "leader": "Officer G. Rao", "members": 16, "specialization": "Search & Rescue", "location": "Sanath Nagar Fire Base", "status": "Available", "assigned_area_id": None, "assigned_area_name": None, "contact_number": "101"},
    {"id": "t_erss_112", "team_name": "Telangana ERSS 112 Rapid Unit", "leader": "Insp. K. V. Reddy", "members": 10, "specialization": "General Relief", "location": "State Command Centre, Banjara Hills", "status": "Available", "assigned_area_id": None, "assigned_area_name": None, "contact_number": "112"},
    {"id": "t_red_health", "team_name": "RED.Health Emergency Ambulance Fleet", "leader": "Fleet Lead S. Verma", "members": 8, "specialization": "Medical", "location": "Madhapur Station", "status": "Available", "assigned_area_id": None, "assigned_area_name": None, "contact_number": "1800 121 911 911"}
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

INITIAL_REPORTS = [
    {
        "id": "rpt_inc_001",
        "incident_id": "INC-DEMO-001",
        "reporter_name": "Traffic Warden - Cyber Towers",
        "reporter_phone": "+91 98490 12345",
        "disaster_type": "Accident",
        "location": "Hitec City IT Corridor (Cyber Towers Junction)",
        "latitude": 17.4504,
        "longitude": 78.3808,
        "people_affected": 3,
        "severity": "High",
        "urgency": "High",
        "required_resources": ["Ambulance", "Emergency Hospital Intake"],
        "assigned_resource_id": "T001 (Telangana 108 Ambulance) & H023 (CARE Hospitals HITEC City)",
        "route_distance_km": 1.8,
        "estimated_arrival_minutes": 5,
        "assignment_status": "Dispatched",
        "description": "Multi-vehicle collision near Cyber Towers flyover with 3 injured. Immediate ALS ambulance dispatched.",
        "status": "In Progress",
        "source": "Emergency Helpline 108",
        "created_at": "2026-10-16T22:15:00Z"
    },
    {
        "id": "rpt_inc_002",
        "incident_id": "INC-DEMO-002",
        "reporter_name": "Resident Welfare Secretary",
        "reporter_phone": "+91 94401 56789",
        "disaster_type": "Flood",
        "location": "Ameerpet / Balkampet Lowland Sector",
        "latitude": 17.4412,
        "longitude": 78.4485,
        "people_affected": 12,
        "severity": "High",
        "urgency": "High",
        "required_resources": ["Rescue Teams", "Ambulance"],
        "assigned_resource_id": "T007 (HYDRAA Disaster Response Force) & T001 (108 Ambulance)",
        "route_distance_km": 3.2,
        "estimated_arrival_minutes": 9,
        "assignment_status": "En Route",
        "description": "Monsoon flash inundation with 1.5m flood depth trapping 12 residents inside ground floor apartments.",
        "status": "In Progress",
        "source": "Citizen SOS Portal",
        "created_at": "2026-10-16T22:18:00Z"
    },
    {
        "id": "rpt_inc_003",
        "incident_id": "INC-DEMO-003",
        "reporter_name": "Station Master Office",
        "reporter_phone": "+91 98480 98765",
        "disaster_type": "Fire",
        "location": "Secunderabad Railway Station Commercial Complex",
        "latitude": 17.4335,
        "longitude": 78.5020,
        "people_affected": 5,
        "severity": "Critical",
        "urgency": "Critical",
        "required_resources": ["Fire and Rescue", "Ambulance"],
        "assigned_resource_id": "T003 (Telangana Fire 101) & H002 (Gandhi Hospital)",
        "route_distance_km": 1.5,
        "estimated_arrival_minutes": 4,
        "assignment_status": "On Scene",
        "description": "Commercial block fire with dense toxic smoke. 5 casualties being stabilized and evacuated to Gandhi Hospital.",
        "status": "Critical",
        "source": "ERSS 112 Dispatch",
        "created_at": "2026-10-16T22:20:00Z"
    }
]

INITIAL_SAFE_LOCATIONS = load_telangana_safe_locations()

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
        # Official Dataset Storage
        self.healthcare_resources = list(INITIAL_HEALTHCARE_RESOURCES)
        self.response_teams = list(INITIAL_RESPONSE_TEAMS)
        self.sample_incidents = list(INITIAL_SAMPLE_INCIDENTS)

    def get_healthcare_resources(self, ownership: str = None, facility_type: str = None):
        res = self.healthcare_resources
        if ownership:
            res = [r for r in res if r.get("ownership", "").lower() == ownership.lower()]
        if facility_type:
            res = [r for r in res if facility_type.lower() in r.get("facility_type", "").lower()]
        return res

    def get_response_teams(self):
        return self.response_teams

    def get_sample_incidents(self):
        return self.sample_incidents

db_store = LocalDatabaseStore()
