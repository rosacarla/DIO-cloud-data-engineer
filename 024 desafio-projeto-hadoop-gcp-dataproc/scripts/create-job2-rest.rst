{
  "reference": {
    "jobId": "8664ee58a79e451880adc5ad60c3e921",
    "projectId": "desafiodataproc-347418"
  },
  "placement": {
    "clusterName": "cluster-dataproc"
  },
  "status": {
    "state": "DONE",
    "stateStartTime": "2022-04-16T21:03:48.262187Z"
  },
  "yarnApplications": [
    {
      "name": "Spark Pi",
      "state": "FINISHED",
      "progress": 1,
      "trackingUrl": "http://cluster-dataproc-m:8088/proxy/application_1650141322018_0002/"
    }
  ],
  "statusHistory": [
    {
      "state": "PENDING",
      "stateStartTime": "2022-04-16T21:03:24.892714Z"
    },
    {
      "state": "SETUP_DONE",
      "stateStartTime": "2022-04-16T21:03:24.951682Z"
    },
    {
      "state": "RUNNING",
      "details": "Agent reported job success",
      "stateStartTime": "2022-04-16T21:03:25.310899Z"
    }
  ],
  "driverControlFilesUri": "gs://dataproc-staging-us-central1-1027639409436-njfmn0cq/google-cloud-dataproc-metainfo/553aa1b5-ee3e-4470-a488-821528e376a2/jobs/8664ee58a79e451880adc5ad60c3e921/",
  "driverOutputResourceUri": "gs://dataproc-staging-us-central1-1027639409436-njfmn0cq/google-cloud-dataproc-metainfo/553aa1b5-ee3e-4470-a488-821528e376a2/jobs/8664ee58a79e451880adc5ad60c3e921/driveroutput",
  "jobUuid": "73066b95-2228-3406-af8c-fab54dd49a5b",
  "done": true,
  "sparkJob": {
    "mainClass": "org.apache.spark.examples.SparkPi",
    "jarFileUris": [
      "file://usr/lib/spark/examples/jars/spark-examples.jar"
    ],
    "args": [
      "1000"
    ]
  }
}