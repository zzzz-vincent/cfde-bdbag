# README

## Design

1. A TSV file exists on disk with the metadata from Neo4J
2. Call `hubmapbags.magic.do_it` on every TSV file from step 1. This creates one folder per dataset and 1 pickle file per dataset with new metadata at the file level.
3. Call `hubmapbags.magic.store` (see ticket 19) on every pickle file from step 2. This will save the entries in the dataframe to a local SQL db. But the trick is that we will add +1 columns to the db. The extra column should be named `UUID`.
4. Call `hubmapbags.magic.get_uuid`. Call this function with a full path, e.g `/full/path/to/file/temp.txt` and check the field `UUID`. If the field is not empty/not null return the value. Else, call the uuid-api, generate the uuid-id, add to the table, and return the value.

## Requirements
* tabulate
* pandas
