gcloud dataproc jobs submit spark \
--cluster=cluster-dataproc \
--region="us-central1" \
--class=org.apache.spark.examples.SparkPi \
--jars=file://usr/lib/spark/examples/jars/spark-examples.jar \
-- 1000