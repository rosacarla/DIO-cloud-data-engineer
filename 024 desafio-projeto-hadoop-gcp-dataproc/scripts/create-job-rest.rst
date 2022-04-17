{
  "reference": {
    "jobId": "job-inicial",
    "projectId": "desafiodataproc-347418"
  },
  "placement": {
    "clusterName": "cluster-dataproc"
  },
  "status": {
    "state": "DONE",
    "stateStartTime": "2022-04-16T20:46:28.498622Z"
  },
  "yarnApplications": [
    {
      "name": "Spark Pi",
      "state": "FINISHED",
      "progress": 1,
      "trackingUrl": "http://cluster-dataproc-m:8088/proxy/application_1650141322018_0001/"
    }
  ],
  "statusHistory": [
    {
      "state": "PENDING",
      "stateStartTime": "2022-04-16T20:45:59.115426Z"
    },
    {
      "state": "SETUP_DONE",
      "stateStartTime": "2022-04-16T20:45:59.170312Z"
    },
    {
      "state": "RUNNING",
      "details": "Agent reported job success",
      "stateStartTime": "2022-04-16T20:45:59.552307Z"
    }
  ],
  "driverControlFilesUri": "gs://dataproc-staging-us-central1-1027639409436-njfmn0cq/google-cloud-dataproc-metainfo/553aa1b5-ee3e-4470-a488-821528e376a2/jobs/job-inicial/",
  "driverOutputResourceUri": "gs://dataproc-staging-us-central1-1027639409436-njfmn0cq/google-cloud-dataproc-metainfo/553aa1b5-ee3e-4470-a488-821528e376a2/jobs/job-inicial/driveroutput",
  "jobUuid": "f925b4f7-66ea-4bd3-aecd-7879af23aee3",
  "done": true,
  "sparkJob": {
    "mainClass": "org.apache.spark.examples.SparkPi",
    "jarFileUris": [
      "file:///usr/lib/spark/examples/jars/spark-examples.jar"
    ],
    "args": [
      "1000"
    ]
  }
}