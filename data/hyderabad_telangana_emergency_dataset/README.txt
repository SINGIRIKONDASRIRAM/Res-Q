HYDERABAD & TELANGANA EMERGENCY RESOURCE DATASET
Created: 2026-10-16
Purpose: Seed data for an academic ResQ / emergency reporting and resource allocation project.

FILES
1. hospitals_hyderabad_telangana.csv
   Government hospitals from the Telangana official directory, plus selected smaller/community hospitals and primary health centres.
2. emergency_response_teams.csv
   Government emergency helplines, HYDRAA DRF and selected private ambulance providers.
3. sample_incident_resource_allocation.csv
   Demo incident rows for testing allocation workflows. These are synthetic examples, not real incidents.
4. sources.csv
   Source URLs and the data each source supports.

IMPORTANT DATA QUALITY NOTES
- This is a starter dataset, not a live emergency dispatch directory.
- Official government hospital contacts are sourced from Telangana government pages.
- Private hospital/clinic details are based on public business listings and must be reconfirmed before real use.
- Small public primary health centres are included, but they should not be assumed to provide 24/7 emergency trauma care.
- Empty latitude/longitude values are intentional. Geocode addresses from a trusted mapping provider and store the date/source of geocoding.
- Bed capacity, current available beds, ambulance count, response time, staffing and dispatch availability are left blank/unknown because live authoritative data was not available.
- Do not convert unknown values to zero or assume a facility can receive a patient.
- Before operational use, validate each phone number, exact address, service hours, emergency capabilities, referral criteria and data-sharing permissions.
- For immediate emergencies in Telangana, use official emergency numbers: 108 (ambulance), 101 (fire), 112 (unified emergency response); Hyderabad District lists 1077 for disaster assistance and 1070 for the State Control Room. See sources.csv.

SUGGESTED DATABASE DESIGN
- Import hospitals_hyderabad_telangana.csv into a `healthcare_resources` table.
- Import emergency_response_teams.csv into an `response_teams` table.
- Keep incident reports and assignments in separate tables, with audit timestamps.
- Use explicit statuses such as VERIFIED, NEEDS_VERIFICATION, AVAILABLE, BUSY, OFFLINE.
- Only mark live availability after an authorized person or API confirms it.

Recommended future columns:
  verified_at, verified_by, data_source, service_radius_km, resource_capabilities,
  current_status, status_updated_at, referral_phone, accepts_ambulance, notes.

This dataset is for software prototyping and should not be used as the sole basis for real-world emergency dispatch.
