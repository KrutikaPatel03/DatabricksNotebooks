# Databricks notebook source
spark.conf.set("fs.azure.account.auth.type.demodatalackstorage.dfs.core.windows.net", "SAS")
spark.conf.set("fs.azure.sas.token.provider.type.demodatalackstorage.dfs.core.windows.net", "org.apache.hadoop.fs.azurebfs.sas.FixedSASTokenProvider")
spark.conf.set("fs.azure.sas.fixed.token.demodatalackstorage.dfs.core.windows.net", "sv=2022-11-02&ss=b&srt=c&sp=rwdlacyx&se=2024-10-23T18:30:40Z&st=2024-10-17T10:30:40Z&spr=https&sig=9KwfSxGdPoyBxOt8gf%2F%2Fq4g2RBJu3FHi3DJw9qcwz1w%3D")


# COMMAND ----------

display(dbutils.fs.ls("abfss://csvconformed@demodatalackstorage.dfs.core.windows.net"))
