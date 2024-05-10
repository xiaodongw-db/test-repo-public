# Databricks notebook source
# MAGIC %sql
# MAGIC
# MAGIC select count(*) from delta.`/mnt/indices/etl/webapp/tree/snapshot/delta`;

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from delta.`/mnt/indices/etl/webapp/tree/snapshot/delta` limit 100;

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC create or replace temporary view view_notebooks as (
# MAGIC select 
# MAGIC   T.database as `database`,
# MAGIC   T.payload.id as id,
# MAGIC   T.payload.type as type, 
# MAGIC   from_json(cast(T.payload.data as string), "name STRING, size INT, reposExportFormat STRING, blobPath STRING, lastSyncedBlobPath STRING, contentSha256Hex STRING, language STRING, created_timestamp BIGINT, updated_timestamp BIGINT") as data
# MAGIC   from delta.`/mnt/indices/etl/webapp/tree/snapshot/delta` T
# MAGIC   where T.payload.type = 'shell'
# MAGIC )

# COMMAND ----------

# MAGIC %sql
# MAGIC select count(*) from view_notebooks where data.blobPath is not null and !(data.blobPath <=> data.lastSyncedBlobPath);

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from view_notebooks where data.blobPath is not null and !(data.blobPath <=> data.lastSyncedBlobPath);

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC drop table if exists search_content_snapshot;

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC select * from search_content_snapshot;
