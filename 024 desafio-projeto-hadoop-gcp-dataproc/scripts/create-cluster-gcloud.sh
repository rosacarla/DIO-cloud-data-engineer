gcloud dataproc clusters create cluster-dataproc --enable-component-gateway --region
us-central1 --zone us-central1-f --master-machine-type n1-standard-4 --master-boot-
disk-size 500 --num-workers 3 --worker-machine-type n1-standard-4 --worker-boot-disk-
size 500 --image-version 2.0-debian10 --optional-components JUPYTER,ZEPPELIN,ZOOKEEPER
--project desafiodataproc-347418
