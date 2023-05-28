import csv
 
data_B = '../OpenClimate/harmonize/data/raw/C2ES_US_ghg_targets/US-states-c2es-targets.csv'

target_id = ''
datasource_id = 'C2ES:US_GHG_targets'
 
with open(data_B, 'r') as csv_in:
    with open('US_states_targets_harmonized.csv', 'w', newline='') as csv_out:
 
        reader_B = csv.reader(csv_in)
        writer_A = csv.writer(csv_out)
        next(reader_B) # header
 
        writer_A.writerow(['target_id', 'actor_id', 'target_type', 'baseline_year', 
            'target_year', 'target_value', 'target_unit', 'URL', 'datasource_id'])
 
        for row in reader_B:
            state = row[0]
            actor_id = row[1]
            target_type = row[2]
            target_value = row[3]
            target_unit = row[4]
            baseline_year = row[5]
            target_year = row[6]
            URL = row[7]
            # generate target_id string
            target_id = f'C2ES:{state}:{target_year}'
            # write to csv
            writer_A.writerow([target_id, actor_id, target_type, baseline_year, 
                target_year, target_value, target_unit, URL, datasource_id])