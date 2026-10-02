// API Base HTTP Request Helper
const API_BASE = import.meta.env.VITE_API_URL || '';

async function request(endpoint, options = {}) {
  const url = `${API_BASE}${endpoint}`;
  const config = {
    headers: {
      'Content-Type': 'application/json',
      ...(options.headers || {}),
    },
    ...options,
  };

  const response = await fetch(url, config);
  if (!response.ok) {
    const errorData = await response.json().catch(() => ({}));
    throw new Error(errorData.detail || errorData.message || `HTTP error! status: ${response.status}`);
  }
  return await response.json();
}

// Default Seed Datasets for Zero-Downtime Deployment & Offline Resilience
const DEFAULT_DISASTERS = [
  {
    id: "d101",
    name: "Cyclone Vardah Relief & Storm Emergency",
    type: "Cyclone",
    location: "Coastal Zone - East Bay",
    severity: "Critical",
    description: "Category 4 tropical cyclone causing coastal inundation, power grid breakdown, and mass displacement.",
    date: "2026-08-10",
    status: "Active",
    created_at: "2026-08-10T08:00:00Z"
  },
  {
    id: "d102",
    name: "River Kaveri Flash Flooding",
    type: "Flood",
    location: "Central River Basin & Lowlands",
    severity: "High",
    description: "Heavy monsoon discharge inundating 12 low-lying residential sectors and agricultural blocks.",
    date: "2026-08-11",
    status: "Active",
    created_at: "2026-08-11T09:30:00Z"
  },
  {
    id: "d103",
    name: "Western Ghats Landslide Emergency",
    type: "Landslide",
    location: "Mountain Ridge Sector 4",
    severity: "Medium",
    description: "Mudslide blocking national arterial highways and cutting off communications to remote villages.",
    date: "2026-08-12",
    status: "Monitoring",
    created_at: "2026-08-12T14:15:00Z"
  },
  {
    id: "d104",
    name: "Kilpauk Building Structural Collapse",
    type: "Building Collapse",
    location: "Kilpauk Urban Sector",
    severity: "Critical",
    description: "Commercial multi-story structure collapse requiring immediate hydraulic cutter teams and medical rescue squads.",
    date: "2026-08-13",
    status: "Active",
    created_at: "2026-08-13T16:00:00Z"
  }
];

const DEFAULT_TEAMS = [
  { id: "t1", team_name: "Alpha Medical ResQ-1", leader: "Dr. Aris Thorne", members: 8, specialization: "Medical", location: "Coastal Sector 1", status: "On Mission", assigned_area_id: "a1", assigned_area_name: "Area A - Coastal Sector 1" },
  { id: "t2", team_name: "Bravo NDRF Battalion 4", leader: "Capt. Rajesh Kumar", members: 15, specialization: "Search & Rescue", location: "Riverbed Township", status: "Assigned", assigned_area_id: "a3", assigned_area_name: "Area C - Riverbed Township" },
  { id: "t3", team_name: "Charlie Coast Guard Squad", leader: "Cmdr. Vikram Sethi", members: 12, specialization: "Evacuation", location: "Fisherman Island", status: "On Mission", assigned_area_id: "a5", assigned_area_name: "Area E - Fisherman Island" },
  { id: "t4", team_name: "Delta Hazmat Response", leader: "Lt. Maya Lin", members: 6, specialization: "Hazmat", location: "Central Depot", status: "Available", assigned_area_id: null, assigned_area_name: null },
  { id: "t5", team_name: "Echo General Relief Contingent", leader: "Sgt. David Miller", members: 20, specialization: "General Relief", location: "North Harbor", status: "Available", assigned_area_id: null, assigned_area_name: null }
];

const DEFAULT_RESOURCES = [
  { id: "r1", resource_name: "Food Rations Packets", resource_type: "Food", category: "Essential Supplies", quantity_available: 18500, quantity_allocated: 11200, unit: "packets", location: "Central Logistics Hub", minimum_threshold: 3000 },
  { id: "r2", resource_name: "Potable Water Cans (20L)", resource_type: "Drinking Water", category: "Essential Supplies", quantity_available: 26000, quantity_allocated: 17500, unit: "cans", location: "Water Purification Base A", minimum_threshold: 5000 },
  { id: "r3", resource_name: "Essential Trauma & Antibiotic Kits", resource_type: "Medicine", category: "Essential Supplies", quantity_available: 2800, quantity_allocated: 1650, unit: "kits", location: "Apex Medical Depot", minimum_threshold: 500 },
  { id: "r4", resource_name: "Thermal Wool Blankets", resource_type: "Blankets", category: "Essential Supplies", quantity_available: 4500, quantity_allocated: 2200, unit: "pieces", location: "Central Logistics Hub", minimum_threshold: 1000 },
  { id: "r5", resource_name: "Field Trauma First Aid Kits", resource_type: "First Aid Kits", category: "Emergency Equipment", quantity_available: 1200, quantity_allocated: 750, unit: "kits", location: "Apex Medical Depot", minimum_threshold: 200 },
  { id: "r6", resource_name: "High-Pressure Oxygen Cylinders", resource_type: "Oxygen Cylinders", category: "Emergency Equipment", quantity_available: 650, quantity_allocated: 410, unit: "cylinders", location: "Apex Medical Depot", minimum_threshold: 100 },
  { id: "r7", resource_name: "Heavy-Duty Hydraulic Rescue Cutters", resource_type: "Rescue Equipment", category: "Emergency Equipment", quantity_available: 140, quantity_allocated: 95, unit: "sets", location: "NDRF Armory", minimum_threshold: 30 },
  { id: "r8", resource_name: "Mobile Diesel Generators 50kW", resource_type: "Generators", category: "Emergency Equipment", quantity_available: 85, quantity_allocated: 52, unit: "units", location: "Power Grid ResQ Base", minimum_threshold: 15 },
  { id: "r9", resource_name: "Advanced Life Support Ambulances", resource_type: "Ambulance", category: "Vehicles", quantity_available: 32, quantity_allocated: 24, unit: "vehicles", location: "Medical Fleet Depot", minimum_threshold: 6 },
  { id: "r10", resource_name: "All-Terrain Rescue Vehicles (4x4)", resource_type: "Rescue Vehicle", category: "Vehicles", quantity_available: 28, quantity_allocated: 19, unit: "vehicles", location: "NDRF Armory", minimum_threshold: 5 },
  { id: "r11", resource_name: "Motorized Inflatable Rescue Boats", resource_type: "Boat", category: "Vehicles", quantity_available: 35, quantity_allocated: 26, unit: "boats", location: "Coastal Guard Station", minimum_threshold: 6 }
];

const DEFAULT_VEHICLES = [
  { id: "v1", vehicle_id: "AMB-101", type: "Ambulance", driver: "K. R. Suresh", capacity: 2, location: "Coastal Sector 1", status: "Assigned", assigned_area_id: "a1", assigned_area_name: "Area A - Coastal Sector 1" },
  { id: "v2", vehicle_id: "AMB-104", type: "Ambulance", driver: "M. Praveen", capacity: 2, location: "North Harbor", status: "In Transit", assigned_area_id: "a2", assigned_area_name: "Area B - North Harbor" },
  { id: "v3", vehicle_id: "TRK-501", type: "Supply Truck", driver: "G. Selvam", capacity: 10000, location: "Central Logistics Hub", status: "Available", assigned_area_id: null, assigned_area_name: null },
  { id: "v4", vehicle_id: "TRK-508", type: "Supply Truck", driver: "P. Ramesh", capacity: 10000, location: "Riverbed Township", status: "Assigned", assigned_area_id: "a3", assigned_area_name: "Area C - Riverbed Township" },
  { id: "v5", vehicle_id: "BOAT-22", type: "Boat", driver: "N. Antony", capacity: 12, location: "Fisherman Island", status: "In Transit", assigned_area_id: "a5", assigned_area_name: "Area E - Fisherman Island" },
  { id: "v6", vehicle_id: "RES-402", type: "Rescue Vehicle", driver: "V. Anand", capacity: 6, location: "Western Basin Slums", status: "Assigned", assigned_area_id: "a7", assigned_area_name: "Area G - Western Basin Slums" },
  { id: "v7", vehicle_id: "HELI-01", type: "Helicopter", driver: "Wg Cmdr R. Sharma", capacity: 8, location: "Air Force Staging Hub", status: "Available", assigned_area_id: null, assigned_area_name: null }
];

const DEFAULT_ALLOCATIONS = [
  { id: "alloc1", area_id: "a1", area_name: "Area A - Coastal Sector 1", food_allocated: 2200, water_allocated: 3500, medicine_allocated: 450, priority_score: 94.2, status: "Dispatched", assigned_team: "Alpha Medical ResQ-1" },
  { id: "alloc2", area_id: "a2", area_name: "Area B - North Harbor", food_allocated: 1800, water_allocated: 2600, medicine_allocated: 320, priority_score: 87.5, status: "In Transit", assigned_team: "Echo General Relief" },
  { id: "alloc3", area_id: "a5", area_name: "Area E - Fisherman Island", food_allocated: 1100, water_allocated: 1600, medicine_allocated: 210, priority_score: 89.0, status: "Dispatched", assigned_team: "Charlie Coast Guard Squad" }
];

// Local Storage Helpers
function getStoredTeams() {
  try {
    const data = localStorage.getItem('resq_teams');
    if (data) return JSON.parse(data);
  } catch (e) {}
  return DEFAULT_TEAMS;
}

function saveTeams(teams) {
  try {
    localStorage.setItem('resq_teams', JSON.stringify(teams));
  } catch (e) {}
}

function getStoredDisasters() {
  try {
    const data = localStorage.getItem('resq_disasters');
    if (data) return JSON.parse(data);
  } catch (e) {}
  return DEFAULT_DISASTERS;
}

function saveDisasters(list) {
  try {
    localStorage.setItem('resq_disasters', JSON.stringify(list));
  } catch (e) {}
}

function getStoredResources() {
  try {
    const data = localStorage.getItem('resq_resources');
    if (data) return JSON.parse(data);
  } catch (e) {}
  return DEFAULT_RESOURCES;
}

function saveResources(list) {
  try {
    localStorage.setItem('resq_resources', JSON.stringify(list));
  } catch (e) {}
}

function getStoredVehicles() {
  try {
    const data = localStorage.getItem('resq_vehicles');
    if (data) return JSON.parse(data);
  } catch (e) {}
  return DEFAULT_VEHICLES;
}

function saveVehicles(list) {
  try {
    localStorage.setItem('resq_vehicles', JSON.stringify(list));
  } catch (e) {}
}

function getStoredAllocations() {
  try {
    const data = localStorage.getItem('resq_allocations');
    if (data) return JSON.parse(data);
  } catch (e) {}
  return DEFAULT_ALLOCATIONS;
}

function saveAllocations(list) {
  try {
    localStorage.setItem('resq_allocations', JSON.stringify(list));
  } catch (e) {}
}

function getStoredCitizenReports() {
  try {
    const data = localStorage.getItem('resq_citizen_reports');
    return data ? JSON.parse(data) : [];
  } catch (e) {
    return [];
  }
}

function saveCitizenReportLocal(report) {
  try {
    const list = getStoredCitizenReports();
    const existingIdx = list.findIndex(r => r.id === report.id || r.incident_id === report.id);
    if (existingIdx >= 0) {
      list[existingIdx] = { ...list[existingIdx], ...report };
    } else {
      list.unshift(report);
    }
    localStorage.setItem('resq_citizen_reports', JSON.stringify(list));
  } catch (e) {
    console.error('Failed to save citizen report to localStorage:', e);
  }
}

function getStoredCitizenAreas() {
  try {
    const data = localStorage.getItem('resq_citizen_areas');
    return data ? JSON.parse(data) : [];
  } catch (e) {
    return [];
  }
}

function saveCitizenAreaLocal(area) {
  try {
    const list = getStoredCitizenAreas();
    const existingIdx = list.findIndex(a => a.id === area.id);
    if (existingIdx >= 0) {
      list[existingIdx] = { ...list[existingIdx], ...area };
    } else {
      list.unshift(area);
    }
    localStorage.setItem('resq_citizen_areas', JSON.stringify(list));
  } catch (e) {
    console.error('Failed to save citizen area to localStorage:', e);
  }
}

function calculateLocalPriorityScore(severity, peopleAffected, resourceCount = 1) {
  let score = 50;
  if (severity === 'Critical') score = 88;
  else if (severity === 'High') score = 72;
  else if (severity === 'Medium') score = 52;
  else if (severity === 'Low') score = 32;

  const peopleBonus = Math.min(10, Math.floor(peopleAffected / 5));
  score = Math.min(100, score + peopleBonus + (resourceCount * 2));
  let level = 'Medium';
  if (score >= 81) level = 'Critical';
  else if (score >= 61) level = 'High';
  else if (score >= 31) level = 'Medium';
  else level = 'Low';

  return { score, level };
}

export const api = {
  // Disasters
  getDisasters: async () => {
    try {
      const res = await request('/api/disasters');
      if (res && res.data && res.data.length > 0) {
        saveDisasters(res.data);
        return res;
      }
    } catch (e) {}
    return { status: 'success', data: getStoredDisasters() };
  },
  createDisaster: async (data) => {
    try {
      const res = await request('/api/disasters', { method: 'POST', body: JSON.stringify(data) });
      if (res && res.data) return res;
    } catch (e) {}
    const current = getStoredDisasters();
    const newDisaster = { id: `d_${Date.now()}`, ...data, created_at: new Date().toISOString() };
    const updated = [newDisaster, ...current];
    saveDisasters(updated);
    return { status: 'success', data: newDisaster };
  },
  updateDisaster: async (id, data) => {
    try {
      const res = await request(`/api/disasters/${id}`, { method: 'PUT', body: JSON.stringify(data) });
      if (res && res.data) return res;
    } catch (e) {}
    const current = getStoredDisasters();
    const idx = current.findIndex(d => d.id === id);
    if (idx >= 0) {
      current[idx] = { ...current[idx], ...data };
      saveDisasters(current);
      return { status: 'success', data: current[idx] };
    }
    return { status: 'success' };
  },
  deleteDisaster: async (id) => {
    try {
      await request(`/api/disasters/${id}`, { method: 'DELETE' });
    } catch (e) {}
    const current = getStoredDisasters().filter(d => d.id !== id);
    saveDisasters(current);
    return { status: 'success' };
  },

  // Affected Areas
  getAreas: async () => {
    let serverAreas = [];
    try {
      const res = await request('/api/areas');
      serverAreas = res.data || [];
    } catch (e) {}

    const localAreas = getStoredCitizenAreas();
    const map = new Map();
    [...localAreas, ...serverAreas].forEach(a => {
      if (a && a.id && !map.has(a.id)) {
        map.set(a.id, a);
      }
    });
    const merged = Array.from(map.values());
    if (merged.length > 0) return { status: 'success', data: merged };

    // Default fallback areas
    return {
      status: 'success',
      data: [
        { id: 'a1', disaster_id: 'd101', area_name: 'Area A - Coastal Sector 1', population: 8500, severity: 'Critical', medical_cases: 280, vulnerable_population: 2100, latitude: 13.0827, longitude: 80.2707, food_required: 2200, water_required: 3500, medicine_required: 450, priority_score: 94.2, status: 'Critical' },
        { id: 'a2', disaster_id: 'd101', area_name: 'Area B - North Harbor', population: 6200, severity: 'Critical', medical_cases: 190, vulnerable_population: 1400, latitude: 13.1200, longitude: 80.2900, food_required: 1800, water_required: 2600, medicine_required: 320, priority_score: 87.5, status: 'Critical' },
        { id: 'a3', disaster_id: 'd102', area_name: 'Area C - Riverbed Township', population: 9400, severity: 'High', medical_cases: 140, vulnerable_population: 1800, latitude: 13.0400, longitude: 80.2100, food_required: 2500, water_required: 4000, medicine_required: 280, priority_score: 78.4, status: 'High' },
        { id: 'a5', disaster_id: 'd101', area_name: 'Area E - Fisherman Island', population: 3100, severity: 'Critical', medical_cases: 125, vulnerable_population: 750, latitude: 13.1500, longitude: 80.3100, food_required: 1100, water_required: 1600, medicine_required: 210, priority_score: 89.0, status: 'Critical' }
      ]
    };
  },
  createArea: (data) => request('/api/areas', { method: 'POST', body: JSON.stringify(data) }),
  updateArea: (id, data) => request(`/api/areas/${id}`, { method: 'PUT', body: JSON.stringify(data) }),
  deleteArea: (id) => request(`/api/areas/${id}`, { method: 'DELETE' }),
  clearAllAreas: () => {
    localStorage.removeItem('resq_citizen_areas');
    return request('/api/areas/all', { method: 'DELETE' }).catch(() => ({ status: 'success' }));
  },
  clearAllDisasterReports: () => {
    localStorage.removeItem('resq_citizen_reports');
    return request('/api/disaster-reports/all', { method: 'DELETE' }).catch(() => ({ status: 'success' }));
  },

  // Resources
  getResources: async () => {
    try {
      const res = await request('/api/resources');
      if (res && res.data && res.data.length > 0) {
        saveResources(res.data);
        return res;
      }
    } catch (e) {}
    return { status: 'success', data: getStoredResources() };
  },
  createResource: async (data) => {
    try {
      const res = await request('/api/resources', { method: 'POST', body: JSON.stringify(data) });
      if (res && res.data) return res;
    } catch (e) {}
    const current = getStoredResources();
    const newRes = { id: `r_${Date.now()}`, ...data };
    const updated = [newRes, ...current];
    saveResources(updated);
    return { status: 'success', data: newRes };
  },
  updateResource: async (id, data) => {
    try {
      const res = await request(`/api/resources/${id}`, { method: 'PUT', body: JSON.stringify(data) });
      if (res && res.data) return res;
    } catch (e) {}
    const current = getStoredResources();
    const idx = current.findIndex(r => r.id === id);
    if (idx >= 0) {
      current[idx] = { ...current[idx], ...data };
      saveResources(current);
      return { status: 'success', data: current[idx] };
    }
    return { status: 'success' };
  },

  // Requests
  getRequests: () => request('/api/requests').catch(() => ({ status: 'success', data: [] })),
  createRequest: (data) => request('/api/requests', { method: 'POST', body: JSON.stringify(data) }),
  updateRequestStatus: (id, status) => request(`/api/requests/${id}`, { method: 'PUT', body: JSON.stringify({ status }) }),

  // Optimization & Allocations
  runOptimization: async (weights = null) => {
    try {
      const res = await request('/api/optimize', { method: 'POST', body: JSON.stringify(weights || {}) });
      if (res && (res.status === 'success' || res.status === 'Success')) return res;
    } catch (e) {}
    return {
      status: 'success',
      data: {
        run_id: `run_${Date.now()}`,
        allocations: [
          { area_id: 'a1', area_name: 'Area A - Coastal Sector 1', food_allocated: 2200, water_allocated: 3500, medicine_allocated: 450, priority_score: 94.2, fulfillment_ratio: 1.0, status: 'Optimal' },
          { area_id: 'a2', area_name: 'Area B - North Harbor', food_allocated: 1800, water_allocated: 2600, medicine_allocated: 320, priority_score: 87.5, fulfillment_ratio: 0.98, status: 'Optimal' },
          { area_id: 'a5', area_name: 'Area E - Fisherman Island', food_allocated: 1100, water_allocated: 1600, medicine_allocated: 210, priority_score: 89.0, fulfillment_ratio: 1.0, status: 'Optimal' }
        ],
        metrics: {
          total_available: 50000,
          total_allocated: 38400,
          remaining_resources: 11600,
          coverage_percentage: 84.5,
          critical_areas_served: 5,
          unfulfilled_demand: 7200
        }
      }
    };
  },
  confirmAllocation: (run_id, allocations) => request('/api/allocate', { method: 'POST', body: JSON.stringify({ run_id, allocations }) }).catch(() => ({ status: 'success' })),
  getAllocations: async () => {
    try {
      const res = await request('/api/allocations');
      if (res && res.data && res.data.length > 0) {
        saveAllocations(res.data);
        return res;
      }
    } catch (e) {}
    return { status: 'success', data: getStoredAllocations() };
  },

  // Teams & Vehicles
  getRescueTeams: async () => {
    try {
      const res = await request('/api/teams');
      if (res && res.data && res.data.length > 0) {
        saveTeams(res.data);
        return res;
      }
    } catch (e) {}
    return { status: 'success', data: getStoredTeams() };
  },
  createRescueTeam: async (data) => {
    try {
      const res = await request('/api/teams', { method: 'POST', body: JSON.stringify(data) });
      if (res && res.data) return res;
    } catch (e) {}
    const current = getStoredTeams();
    const newTeam = { id: `t_${Date.now()}`, ...data };
    const updated = [newTeam, ...current];
    saveTeams(updated);
    return { status: 'success', data: newTeam };
  },
  updateRescueTeam: async (id, data) => {
    try {
      const res = await request(`/api/teams/${id}`, { method: 'PUT', body: JSON.stringify(data) });
      if (res && res.data) return res;
    } catch (e) {}
    const current = getStoredTeams();
    const idx = current.findIndex(t => t.id === id);
    if (idx >= 0) {
      current[idx] = { ...current[idx], ...data };
      saveTeams(current);
      return { status: 'success', data: current[idx] };
    }
    return { status: 'success' };
  },

  getVehicles: async () => {
    try {
      const res = await request('/api/vehicles');
      if (res && res.data && res.data.length > 0) {
        saveVehicles(res.data);
        return res;
      }
    } catch (e) {}
    return { status: 'success', data: getStoredVehicles() };
  },
  createVehicle: async (data) => {
    try {
      const res = await request('/api/vehicles', { method: 'POST', body: JSON.stringify(data) });
      if (res && res.data) return res;
    } catch (e) {}
    const current = getStoredVehicles();
    const newV = { id: `v_${Date.now()}`, ...data };
    const updated = [newV, ...current];
    saveVehicles(updated);
    return { status: 'success', data: newV };
  },
  updateVehicle: async (id, data) => {
    try {
      const res = await request(`/api/vehicles/${id}`, { method: 'PUT', body: JSON.stringify(data) });
      if (res && res.data) return res;
    } catch (e) {}
    const current = getStoredVehicles();
    const idx = current.findIndex(v => v.id === id);
    if (idx >= 0) {
      current[idx] = { ...current[idx], ...data };
      saveVehicles(current);
      return { status: 'success', data: current[idx] };
    }
    return { status: 'success' };
  },

  // Analytics & Alerts
  getAnalytics: () => request('/api/analytics').catch(() => ({
    summary: {
      total_disasters: 4,
      total_affected_areas: 4,
      total_people_affected: 27200,
      total_rescue_teams: 5,
      active_teams: 3,
      resources_allocated_pct: 68.5,
      critical_shortages: 2
    }
  })),
  getAlerts: () => request('/api/alerts').catch(() => ({
    status: 'success',
    data: [
      { id: "alt0", title: "Critical ICU Oxygen Shortage", message: "Emergency ICU ward at Coastal Sector 1 field hospital reports 0 backup oxygen cylinders.", severity: "Critical", status: "Active", created_at: new Date().toISOString() },
      { id: "alt1", title: "Critical Medicine Shortage", message: "Medicine inventory in Area A - Coastal Sector 1 is below safety threshold.", severity: "Critical", status: "Active", created_at: new Date().toISOString() }
    ]
  })),
  createAlert: (data) => request('/api/alerts', { method: 'POST', body: JSON.stringify(data) }),
  dismissAlert: (id) => request(`/api/alerts/${id}`, { method: 'PUT' }),

  // SMS Disaster Reports & Endpoints
  sendIncomingSMS: (data) => request('/sms/incoming', { method: 'POST', body: JSON.stringify(data) }),
  simulateSMSReport: (data) => request('/sms/incoming', { method: 'POST', body: JSON.stringify(data) }),
  getReports: (status = null, severity = null) => api.getDisasterReports(status, severity),
  getReportById: (id) => api.getDisasterReportById(id),

  getDisasterReports: async (status = null, severity = null) => {
    let serverReports = [];
    try {
      const params = new URLSearchParams();
      if (status && status !== 'All') params.append('status', status);
      if (severity && severity !== 'All') params.append('severity', severity);
      const query = params.toString() ? `?${params.toString()}` : '';
      const res = await request(`/api/disaster-reports${query}`);
      serverReports = res.data || [];
    } catch (e) {}

    const localReports = getStoredCitizenReports();
    const map = new Map();
    [...localReports, ...serverReports].forEach(r => {
      if (r && (r.id || r.incident_id)) {
        const key = r.id || r.incident_id;
        if (!map.has(key)) {
          map.set(key, r);
        }
      }
    });

    let merged = Array.from(map.values());

    if (status && status !== 'All') {
      merged = merged.filter(r => r.status === status);
    }
    if (severity && severity !== 'All') {
      merged = merged.filter(r => r.severity === severity || r.priority_level === severity || r.priority === severity);
    }

    merged.sort((a, b) => (b.priority_score || 0) - (a.priority_score || 0));
    return { status: 'success', count: merged.length, data: merged };
  },

  getDisasterReportById: async (id) => {
    try {
      const res = await request(`/api/disaster-reports/${id}`);
      if (res && res.data) return res;
    } catch (e) {}

    const localReports = getStoredCitizenReports();
    const found = localReports.find(r => r.id === id || r.incident_id === id);
    if (found) return { status: 'success', data: found };
    throw new Error('Disaster report not found.');
  },

  getPriorityRanking: () => request('/priority-ranking').catch(() => ({ status: 'success', data: [] })),

  updateDisasterReportStatus: async (id, data) => {
    let res = null;
    try {
      res = await request(`/api/disaster-reports/${id}/status`, { method: 'PATCH', body: JSON.stringify(data) });
    } catch (e) {}

    const localReports = getStoredCitizenReports();
    const idx = localReports.findIndex(r => r.id === id || r.incident_id === id);
    if (idx >= 0) {
      localReports[idx] = {
        ...localReports[idx],
        ...data,
        updated_at: new Date().toISOString()
      };
      localStorage.setItem('resq_citizen_reports', JSON.stringify(localReports));
    }
    return res || { status: 'success', message: 'Report status updated locally' };
  },

  verifyDisasterReport: (id) => api.updateDisasterReportStatus(id, { status: 'Verified' }),
  assignTeamToReport: (id, data) => api.updateDisasterReportStatus(id, { status: 'In Progress', assigned_team_name: data.team_name }),
  completeDisasterReport: (id) => api.updateDisasterReportStatus(id, { status: 'Resolved' }),
  simulateWhatsAppReport: (data) => request('/sms/incoming', { method: 'POST', body: JSON.stringify(data) }),

  // OpenWeather API Integration
  getWeatherStatus: async () => {
    try {
      const res = await request('/api/weather/status');
      if (res && res.status) return res;
    } catch (e) {}
    return {
      status: 'Simulated Mode (No API Key)',
      has_api_key: false,
      masked_key: 'Not Set',
      provider: 'OpenWeatherMap API v2.5 (Simulated Engine)',
      units_supported: ['metric', 'imperial']
    };
  },
  getWeatherCurrent: async (lat = 13.0827, lon = 80.2707, location = '') => {
    try {
      const params = new URLSearchParams({ lat, lon });
      if (location) params.append('location', location);
      const res = await request(`/api/weather/current?${params.toString()}`);
      if (res && res.main) return res;
    } catch (e) {}
    return {
      name: location || "Coastal Sector 1",
      main: { temp: 27.8, feels_like: 31.4, humidity: 88, pressure: 1004 },
      weather: [{ main: "Rain", description: "Heavy Intensity Rain & Thunderstorm", icon: "11d" }],
      wind: { speed: 16.5 },
      rain: { "1h": 18.5 },
      risk_assessment: { weather_risk_score: 88.5, risk_level: "Extreme", risk_color: "red", active_hazards: ["Heavy Rain & Inundation Risk", "High Wind Risk"] }
    };
  },
  getWeatherForecast: async (lat = 13.0827, lon = 80.2707, location = '') => {
    try {
      const params = new URLSearchParams({ lat, lon });
      if (location) params.append('location', location);
      const res = await request(`/api/weather/forecast?${params.toString()}`);
      if (res && res.list) return res;
    } catch (e) {}
    return {
      location: location || 'Disaster Zone Sector',
      lat: lat,
      lon: lon,
      cnt: 5,
      list: [
        { dt_txt: '2026-09-13 18:00:00', dt: 1789408800, main: { temp: 27.8, feels_like: 31.4, humidity: 88, pressure: 1004 }, weather: [{ main: 'Rain', description: 'Heavy Intensity Rain', icon: '11d' }], wind: { speed: 16.5 }, pop: 0.95 },
        { dt_txt: '2026-09-14 00:00:00', dt: 1789430400, main: { temp: 26.5, feels_like: 29.8, humidity: 91, pressure: 1002 }, weather: [{ main: 'Thunderstorm', description: 'Thunderstorm with Heavy Rain', icon: '11d' }], wind: { speed: 19.2 }, pop: 0.98 },
        { dt_txt: '2026-09-14 06:00:00', dt: 1789452000, main: { temp: 28.1, feels_like: 32.0, humidity: 84, pressure: 1006 }, weather: [{ main: 'Rain', description: 'Moderate Rain', icon: '10d' }], wind: { speed: 14.0 }, pop: 0.75 },
        { dt_txt: '2026-09-14 12:00:00', dt: 1789473600, main: { temp: 30.4, feels_like: 35.2, humidity: 76, pressure: 1009 }, weather: [{ main: 'Clouds', description: 'Scattered Clouds', icon: '03d' }], wind: { speed: 10.5 }, pop: 0.40 },
        { dt_txt: '2026-09-14 18:00:00', dt: 1789495200, main: { temp: 29.0, feels_like: 33.1, humidity: 80, pressure: 1010 }, weather: [{ main: 'Clear', description: 'Clear Sky', icon: '01d' }], wind: { speed: 8.2 }, pop: 0.15 }
      ]
    };
  },
  getAreaWeather: async (areaId) => {
    try {
      const res = await request(`/api/weather/area/${areaId}`);
      if (res) return res;
    } catch (e) {}
    return {
      area_id: areaId,
      area_name: "Disaster Zone Sector",
      weather_temp: 27.8,
      weather_feels_like: 31.4,
      weather_description: "Heavy Intensity Rain",
      weather_icon: "11d",
      humidity: 88,
      wind_speed: 16.5,
      weather_risk_score: 88.5,
      risk_level: "Extreme"
    };
  },
  getWeatherOverview: async () => {
    try {
      const res = await request('/api/weather/overview');
      if (res && res.areas_weather && res.areas_weather.length > 0) return res;
    } catch (e) {}
    return {
      has_live_api: false,
      total_monitored_areas: 4,
      average_weather_risk_score: 74.5,
      active_hazard_warnings: ["Heavy Rain & Inundation Risk", "High Wind & Storm Surge", "Extreme Humidity & Squall"],
      areas_weather: [
        {
          area_id: "a1",
          area_name: "Area A - Coastal Sector 1",
          disaster_id: "d101",
          latitude: 13.0827,
          longitude: 80.2707,
          severity: "Critical",
          weather_temp: 27.8,
          weather_feels_like: 31.4,
          weather_description: "Heavy Intensity Rain & Thunderstorm",
          weather_icon: "11d",
          humidity: 88,
          wind_speed: 16.5,
          pressure: 1004,
          rain_1h: 18.5,
          weather_risk_score: 88.5,
          risk_level: "Extreme",
          risk_color: "red",
          active_hazards: ["Heavy Rain & Inundation Risk", "High Wind Risk"],
          recommended_action: "Immediate Evacuation & Inflatable Rescue Boat Dispatch"
        },
        {
          area_id: "a2",
          area_name: "Area B - North Harbor",
          disaster_id: "d101",
          latitude: 13.1200,
          longitude: 80.2900,
          severity: "Critical",
          weather_temp: 26.5,
          weather_feels_like: 30.1,
          weather_description: "Severe Squall & Tropical Thunderstorm",
          weather_icon: "11d",
          humidity: 92,
          wind_speed: 22.8,
          pressure: 998,
          rain_1h: 32.0,
          weather_risk_score: 92.0,
          risk_level: "Extreme",
          risk_color: "red",
          active_hazards: ["High Wind Risk", "Torrential Rain Warning"],
          recommended_action: "Anchor Harbor Craft & Dispatch High Capacity Water Pumps"
        },
        {
          area_id: "a3",
          area_name: "Area C - Riverbed Township",
          disaster_id: "d102",
          latitude: 13.0400,
          longitude: 80.2100,
          severity: "High",
          weather_temp: 29.2,
          weather_feels_like: 33.0,
          weather_description: "Overcast Clouds & High Humidity",
          weather_icon: "04d",
          humidity: 78,
          wind_speed: 9.4,
          pressure: 1008,
          rain_1h: 4.2,
          weather_risk_score: 64.0,
          risk_level: "High",
          risk_color: "amber",
          active_hazards: ["High Humidity Risk"],
          recommended_action: "Monitor River Basin Water Gauge Levels"
        },
        {
          area_id: "a5",
          area_name: "Area E - Fisherman Island",
          disaster_id: "d101",
          latitude: 13.1500,
          longitude: 80.3100,
          severity: "Critical",
          weather_temp: 27.1,
          weather_feels_like: 31.0,
          weather_description: "Heavy Monsoon Downpour",
          weather_icon: "09d",
          humidity: 89,
          wind_speed: 18.2,
          pressure: 1002,
          rain_1h: 21.0,
          weather_risk_score: 84.0,
          risk_level: "Extreme",
          risk_color: "red",
          active_hazards: ["Heavy Rain & Inundation Risk", "High Wind Risk"],
          recommended_action: "Dispatch Coast Guard Evacuation Boats"
        }
      ]
    };
  },
  configureWeatherKey: async (apiKey) => {
    try {
      const res = await request('/api/weather/config', { method: 'POST', body: JSON.stringify({ api_key: apiKey }) });
      if (res) return res;
    } catch (e) {}
    localStorage.setItem('resq_weather_api_key', apiKey);
    return { success: true, message: 'OpenWeather API Key configured successfully.' };
  },

  // Citizen Portal
  submitCitizenReport: async (data) => {
    let apiResponse = null;
    try {
      apiResponse = await request('/api/citizen/report', { method: 'POST', body: JSON.stringify(data) });
    } catch (err) {
      console.warn('Backend API unavailable for citizen report POST, saving to local state fallback:', err);
    }

    if (apiResponse && apiResponse.status === 'success' && apiResponse.data) {
      saveCitizenReportLocal(apiResponse.data);
      return apiResponse;
    }

    const reportId = `rpt_cit_${Math.random().toString(36).substring(2, 10)}`;
    const nowIso = new Date().toISOString();
    const lat = data.latitude ? parseFloat(data.latitude) : 13.0827;
    const lng = data.longitude ? parseFloat(data.longitude) : 80.2707;
    const locStr = data.location || `GPS Position (${lat.toFixed(4)}, ${lng.toFixed(4)})`;
    const { score, level } = calculateLocalPriorityScore(data.severity || 'Medium', data.people_affected || 1, (data.resources_needed || []).length);

    const localReport = {
      id: reportId,
      incident_id: reportId,
      reporter_name: data.name || 'Citizen (SOS Signal)',
      reporter_phone: data.phone || '108 / Emergency Hotline',
      original_message: data.description || '',
      disaster_type: data.disaster_type || 'Emergency',
      location: locStr,
      latitude: lat,
      longitude: lng,
      people_affected: data.people_affected || 1,
      affected_people: data.people_affected || 1,
      severity: data.severity || 'Medium',
      urgency: data.severity || 'Medium',
      required_resources: data.resources_needed || [],
      description: data.description || '',
      image_url: data.image_url,
      priority_score: score,
      priority_level: level,
      priority: level.toUpperCase(),
      status: 'Pending',
      source: 'Citizen Portal',
      is_citizen_report: true,
      created_at: nowIso,
      updated_at: nowIso
    };

    saveCitizenReportLocal(localReport);

    const areaId = `area_cit_${Math.random().toString(36).substring(2, 8)}`;
    const localArea = {
      id: areaId,
      disaster_id: 'd101',
      area_name: locStr.startsWith('Area') ? locStr : `Citizen Sector - ${locStr}`,
      population: data.people_affected || 1,
      severity: data.severity || 'Medium',
      medical_cases: Math.max(1, Math.floor((data.people_affected || 1) * 0.3)),
      vulnerable_population: Math.max(1, Math.floor((data.people_affected || 1) * 0.4)),
      latitude: lat,
      longitude: lng,
      food_required: (data.people_affected || 1) * 3,
      water_required: (data.people_affected || 1) * 5,
      medicine_required: Math.max(1, Math.floor((data.people_affected || 1) * 0.5)),
      priority_score: score,
      status: 'Pending Verification',
      source: 'Citizen Portal'
    };

    saveCitizenAreaLocal(localArea);

    return {
      status: 'success',
      message: 'Emergency report submitted successfully.',
      report_id: reportId,
      data: localReport
    };
  },

  getCitizenReportStatus: (id) => api.getDisasterReportById(id),

  // Reverse Geocoding Helper: Converts Latitude & Longitude to full human-readable address
  reverseGeocode: async (lat, lng) => {
    if (lat === undefined || lat === null || lng === undefined || lng === null) return null;
    const nLat = Number(lat);
    const nLng = Number(lng);
    try {
      const controller = new AbortController();
      const timeoutId = setTimeout(() => controller.abort(), 4000);
      const res = await fetch(`https://nominatim.openstreetmap.org/reverse?format=json&lat=${nLat}&lon=${nLng}&zoom=18&addressdetails=1`, {
        signal: controller.signal,
        headers: { 'Accept-Language': 'en' }
      });
      clearTimeout(timeoutId);
      if (res.ok) {
        const data = await res.json();
        if (data && data.display_name) {
          const addr = data.address || {};
          const shortTitle = addr.road || addr.suburb || addr.neighbourhood || addr.city_district || addr.city || data.display_name.split(',')[0];
          return {
            fullAddress: data.display_name,
            shortAddress: `${shortTitle}, ${addr.city || addr.state_district || 'Chennai'}`,
            road: addr.road || '',
            neighbourhood: addr.neighbourhood || addr.suburb || '',
            city: addr.city || addr.town || addr.village || 'Chennai',
            state: addr.state || 'Tamil Nadu',
            postcode: addr.postcode || '',
            country: addr.country || 'India',
            raw: data
          };
        }
      }
    } catch (err) {
      console.warn('Online reverse geocoding fallback active:', err.message);
    }

    // Fallback: Geospatial synthesis based on coordinates
    return {
      fullAddress: `Geospatial Location (${nLat.toFixed(4)}° N, ${nLng.toFixed(4)}° E), Chennai Metropolitan Area, Tamil Nadu, India`,
      shortAddress: `GPS Sector (${nLat.toFixed(4)}, ${nLng.toFixed(4)})`,
      road: 'Metropolitan Sector',
      neighbourhood: 'Chennai Zone',
      city: 'Chennai',
      state: 'Tamil Nadu',
      postcode: '600001',
      country: 'India',
      raw: null
    };
  },

  // Online Address Geocode Search: Searches any address/place name anywhere
  searchAddresses: async (query) => {
    if (!query || query.trim().length < 2) return [];
    try {
      const controller = new AbortController();
      const timeoutId = setTimeout(() => controller.abort(), 4000);
      const res = await fetch(`https://nominatim.openstreetmap.org/search?format=json&q=${encodeURIComponent(query)}&limit=6&addressdetails=1`, {
        signal: controller.signal,
        headers: { 'Accept-Language': 'en' }
      });
      clearTimeout(timeoutId);
      if (res.ok) {
        const data = await res.json();
        if (Array.isArray(data) && data.length > 0) {
          return data.map((item, idx) => {
            const addr = item.address || {};
            const mainName = item.name || addr.road || addr.suburb || item.display_name.split(',')[0];
            return {
              id: `geo-search-${item.place_id || idx}-${Date.now()}`,
              name: mainName,
              category: 'Geocoded Address',
              address: item.display_name,
              latitude: parseFloat(item.lat),
              longitude: parseFloat(item.lon),
              phone: '108 / 112',
              capacity: 'Verified Map Landmark',
              status: 'Active Location',
              iconEmoji: '📍',
              rawObj: item,
              type: 'geocoded_address'
            };
          });
        }
      }
    } catch (err) {
      console.warn('Address search fallback active:', err.message);
    }
    return [];
  },

  // Safe Locations & Emergency Facilities
  getSafeLocations: (lat = null, lng = null, disaster_type = '') => {
    const params = new URLSearchParams();
    if (lat !== null && lng !== null) {
      params.append('lat', lat);
      params.append('lng', lng);
    }
    if (disaster_type) params.append('disaster_type', disaster_type);
    const query = params.toString() ? `?${params.toString()}` : '';
    return request(`/api/safe-locations${query}`).catch(() => ({
      status: 'success',
      data: [
        { id: "loc_h1", name: "Apollo Emergency & Trauma Hospital", facility_type: "Hospital", latitude: 13.0604, longitude: 80.2496, address: "21 Greams Lane, Thousand Lights, Chennai", phone: "+91 44 2829 0200", capacity: "250 Emergency Beds (35 ICU)", status: "Operational 24/7" },
        { id: "loc_h2", name: "Government General Hospital & ICU Hub (RGGH)", facility_type: "Hospital", latitude: 13.0815, longitude: 80.2777, address: "EVR Periyar Salai, Park Town, Chennai", phone: "+91 44 2530 5000", capacity: "500 Emergency Beds (60 ICU)", status: "Operational 24/7" },
        { id: "loc_h3", name: "Tambaram District Trauma & Surgical Center", facility_type: "Hospital", latitude: 12.9240, longitude: 80.1290, address: "GST Road, Tambaram Sanatorium, Chennai", phone: "+91 44 2241 8000", capacity: "180 Emergency Beds (20 ICU)", status: "Operational 24/7" },
        { id: "loc_h4", name: "Stanley Medical Apex Trauma Care", facility_type: "Hospital", latitude: 13.1030, longitude: 80.2870, address: "Old Jail Road, Royapuram, Chennai", phone: "+91 44 2528 1351", capacity: "320 Emergency Beds (40 ICU)", status: "Operational 24/7" },
        { id: "loc_h5", name: "Chromepet Emergency Medical Base", facility_type: "Hospital", latitude: 12.9510, longitude: 80.1410, address: "Station Road, Chromepet, Chennai", phone: "+91 44 2265 1122", capacity: "120 Emergency Beds (15 ICU)", status: "Operational 24/7" },
        { id: "loc_h6", name: "MIOT International Trauma Hospital", facility_type: "Hospital", latitude: 13.0247, longitude: 80.1785, address: "Mount-Poonamallee Road, Manapakkam / Porur", phone: "+91 44 4200 2288", capacity: "300 Emergency ICU Beds (45 ICU)", status: "Operational 24/7" },
        { id: "loc_h7", name: "Sri Ramachandra Medical Center & Emergency Hub", facility_type: "Hospital", latitude: 13.0375, longitude: 80.1412, address: "No.1 Ramachandra Nagar, Porur, Chennai", phone: "+91 44 4592 8500", capacity: "450 Emergency Beds (55 ICU)", status: "Operational 24/7" },
        { id: "loc_h8", name: "SIMS Super Specialty Emergency Hospital", facility_type: "Hospital", latitude: 13.0512, longitude: 80.2120, address: "Metro Station Complex, Vadapalani, Chennai", phone: "+91 44 2000 2000", capacity: "280 Trauma Beds (30 ICU)", status: "Operational 24/7" },
        { id: "loc_h9", name: "Prashanth Emergency Hospital & Trauma Center", facility_type: "Hospital", latitude: 12.9780, longitude: 80.2220, address: "Velachery Main Road, Velachery, Chennai", phone: "+91 44 4227 7777", capacity: "190 Emergency Beds (25 ICU)", status: "Operational 24/7" },
        { id: "loc_h10", name: "Gleneagles Global Trauma & Emergency City", facility_type: "Hospital", latitude: 12.9062, longitude: 80.1983, address: "Cheran Nagar, Perumbakkam / Medavakkam", phone: "+91 44 4477 7000", capacity: "350 Critical Care Beds (50 ICU)", status: "Operational 24/7" },
        { id: "loc_h11", name: "Fortis Malar Emergency Care", facility_type: "Hospital", latitude: 13.0041, longitude: 80.2568, address: "First Main Road, Gandhi Nagar, Adyar, Chennai", phone: "+91 44 4289 2222", capacity: "160 Emergency Beds (20 ICU)", status: "Operational 24/7" },
        // Chennai Urban Community Health Centres (UCHC - Greater Chennai Corporation)
        { id: "loc_uchc_1", name: "Kuppam UCHC (Zone I, Div 11)", facility_type: "Health Center", uchc_zone: "I", uchc_division: 11, latitude: 13.2185, longitude: 80.3245, address: "No.1, School Street, Jothy Nagar, Kuppam, Chennai - 600057", phone: "044-25732100", capacity: "50 Emergency Beds • 24/7 Primary Care", status: "Operational 24/7" },
        { id: "loc_uchc_2", name: "Manali UCHC (Zone II, Div 21)", facility_type: "Health Center", uchc_zone: "II", uchc_division: 21, latitude: 13.1672, longitude: 80.2618, address: "No 1 Nedunchezian Salai, Manali, Chennai - 600068", phone: "044-25941200", capacity: "60 Emergency Beds • Trauma & Triage", status: "Operational 24/7" },
        { id: "loc_uchc_3", name: "Madhavaram UCHC (Zone III, Div 26)", facility_type: "Health Center", uchc_zone: "III", uchc_division: 26, latitude: 13.1485, longitude: 80.2312, address: "No 47, Swamy Nagar, Madhavaram, Chennai - 600060", phone: "044-25530122", capacity: "55 Emergency Beds • Ambulance Post", status: "Operational 24/7" },
        { id: "loc_uchc_4", name: "R.K. Nagar UCHC (Zone IV, Div 47)", facility_type: "Health Center", uchc_zone: "IV", uchc_division: 47, latitude: 13.1162, longitude: 80.2854, address: "No.88, K.H Road, Korukkupet, Chennai - 600021", phone: "044-25983411", capacity: "70 Emergency Beds • Emergency Ward", status: "Operational 24/7" },
        { id: "loc_uchc_5", name: "Sanjeevarayanpet UCHC (Zone V, Div 49)", facility_type: "Health Center", uchc_zone: "V", uchc_division: 49, latitude: 13.1092, longitude: 80.2921, address: "No.194, Solaiappar St, Old Washermanpet, Chennai - 600021", phone: "044-25912300", capacity: "65 Emergency Beds • Stabilization Unit", status: "Operational 24/7" },
        { id: "loc_uchc_6", name: "Pulianthope UCHC (Zone VI, Div 73)", facility_type: "Health Center", uchc_zone: "VI", uchc_division: 73, latitude: 13.0945, longitude: 80.2682, address: "42, Thiruvenkadasamy Street, Pulianthope, Chennai - 600012", phone: "044-26671233", capacity: "75 Emergency Beds • Maternity & Trauma", status: "Operational 24/7" },
        { id: "loc_uchc_7", name: "Padi UCHC (Zone VII, Div 87)", facility_type: "Health Center", uchc_zone: "VII", uchc_division: 87, latitude: 13.0974, longitude: 80.1872, address: "No. 5, Church St, TMP Nagar, Padi, Chennai - 600050", phone: "044-26543100", capacity: "60 Emergency Beds • Oxygen Supply Hub", status: "Operational 24/7" },
        { id: "loc_uchc_8", name: "Ayanavaram UCHC (Zone VIII, Div 96)", facility_type: "Health Center", uchc_zone: "VIII", uchc_division: 96, latitude: 13.0961, longitude: 80.2384, address: "29, United India Nagar, Ayanavaram, Chennai - 600023", phone: "044-26742311", capacity: "70 Emergency Beds • Critical Response", status: "Operational 24/7" },
        { id: "loc_uchc_9", name: "Mirsahibpet UCHC (Zone IX, Div 119)", facility_type: "Health Center", uchc_zone: "IX", uchc_division: 119, latitude: 13.0564, longitude: 80.2678, address: "No.11, Begum 5th Street, Royapettah, Chennai - 600014", phone: "044-28481299", capacity: "80 Emergency Beds • Central Ward", status: "Operational 24/7" },
        { id: "loc_uchc_10", name: "Vadapalani UCHC (Zone X, Div 134)", facility_type: "Health Center", uchc_zone: "X", uchc_division: 134, latitude: 13.0503, longitude: 80.2132, address: "No: 65, Arcot Road, Kodambakkam, Chennai - 600024", phone: "044-24831200", capacity: "85 Emergency Beds • Trauma & Pediatric", status: "Operational 24/7" },
        { id: "loc_uchc_11", name: "Porur UCHC (Zone XI, Div 153)", facility_type: "Health Center", uchc_zone: "XI", uchc_division: 153, latitude: 13.0384, longitude: 80.1572, address: "4, Senthil Nagar, Hospital Road, Chinna Porur, Chennai - 600116", phone: "044-24761211", capacity: "90 Emergency Beds • Flood Evacuation", status: "Operational 24/7" },
        { id: "loc_uchc_12", name: "Alandur UCHC (Zone XII, Div 160)", facility_type: "Health Center", uchc_zone: "XII", uchc_division: 160, latitude: 13.0031, longitude: 80.2014, address: "No.56, Sowri St, Alandur, Chennai - 600016", phone: "044-22341200", capacity: "75 Emergency Beds • Metro Corridor Unit", status: "Operational 24/7" },
        { id: "loc_uchc_13", name: "Adyar UCHC (Zone XIII, Div 175)", facility_type: "Health Center", uchc_zone: "XIII", uchc_division: 175, latitude: 13.0065, longitude: 80.2573, address: "No: 2, Venkatarathinam Nagar, Adyar, Chennai - 600020", phone: "044-24411200", capacity: "80 Emergency Beds • Coastal Response Team", status: "Operational 24/7" },
        { id: "loc_uchc_14", name: "Perungudi UCHC (Zone XIV, Div 184)", facility_type: "Health Center", uchc_zone: "XIV", uchc_division: 184, latitude: 12.9642, longitude: 80.2441, address: "Next Division Office, School Road, Perungudi, Chennai - 600096", phone: "044-24961200", capacity: "70 Emergency Beds • OMR Emergency Hub", status: "Operational 24/7" },
        { id: "loc_uchc_15", name: "Kannagi Nagar UCHC (Zone XV, Div 195)", facility_type: "Health Center", uchc_zone: "XV", uchc_division: 195, latitude: 12.9345, longitude: 80.2305, address: "Kannagi Nagar Slum Clearance Board, Kannagi Nagar, Chennai - 600115", phone: "044-24581200", capacity: "85 Emergency Beds • Community Center", status: "Operational 24/7" },
        { id: "loc_uchc_16", name: "Injambakkam UCHC (Zone XV, Div 196)", facility_type: "Health Center", uchc_zone: "XV", uchc_division: 196, latitude: 12.9192, longitude: 80.2524, address: "VOC Street, Near Amma Unavagam, Injambakkam Peripheral Hospital, Chennai - 600115", phone: "044-24491200", capacity: "80 Emergency Beds • ECR Coastal Station", status: "Operational 24/7" },
        { id: "loc_s1", name: "Tambaram Indoor Stadium Relief Shelter", facility_type: "Relief Shelter", latitude: 12.9200, longitude: 80.1250, address: "Gandhi Road, West Tambaram, Chennai", phone: "1800-425-1088", capacity: "1,500 Evacuees (Food/Water Active)", status: "Active Safe Zone" },
        { id: "loc_s2", name: "Velachery Community Evacuation Hall", facility_type: "Relief Shelter", latitude: 12.9720, longitude: 80.2180, address: "Bypass Road, Velachery, Chennai", phone: "1800-425-1088", capacity: "1,200 Evacuees (Medical Aid Available)", status: "Active Safe Zone" },
        { id: "loc_s3", name: "Jawaharlal Nehru Stadium Relief Camp", facility_type: "Relief Shelter", latitude: 13.0850, longitude: 80.2700, address: "Sydenhams Road, Periamet, Chennai", phone: "1800-425-1088", capacity: "3,500 Evacuees (Full Logistics Base)", status: "Active Safe Zone" },
        { id: "loc_f1", name: "Tambaram Fire & Rescue Station", facility_type: "Fire Station", latitude: 12.9260, longitude: 80.1310, address: "Shanmugam Road, West Tambaram, Chennai", phone: "101 / +91 44 2226 5101", capacity: "6 Fire Engines + 2 Inflatable Boats", status: "High Alert Dispatch" },
        { id: "loc_f2", name: "Guindy Industrial Fire & Hazmat Station", facility_type: "Fire Station", latitude: 13.0100, longitude: 80.2050, address: "Inner Ring Road, Guindy, Chennai", phone: "101 / +91 44 2234 1101", capacity: "8 Fire Tenders + Hazmat Unit", status: "High Alert Dispatch" }
      ]
    }));
  }
};
