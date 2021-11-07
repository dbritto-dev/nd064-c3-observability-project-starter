# Installing Helm

```sh
curl https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3 | bash
```

# Installing Prometheus

```sh
kubectl create namespace monitoring
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo add stable https://charts.helm.sh/stable
helm repo update
helm install prometheus prometheus-community/kube-prometheus-stack -n monitoring --kubeconfig /etc/rancher/k3s/k3s.yaml
```

# Verify Prometheus

```sh
kubectl get pods,svc -n monitoring
```

# Forwarding Prometheus

```sh
kubectl port-forward svc/prometheus-grafana --address 0.0.0.0 3000:80 -n monitoring
```

# Accessing to Grafana Dashboard

Go to http://localhost:3000

```yml
username: admin 
password: prom-operator
```

# Installing jaeger

```sh
kubectl create namespace observability
kubectl create -f https://raw.githubusercontent.com/jaegertracing/jaeger-operator/master/deploy/crds/jaegertracing.io_jaegers_crd.yaml
kubectl create -n observability -f https://raw.githubusercontent.com/jaegertracing/jaeger-operator/master/deploy/service_account.yaml
kubectl create -n observability -f https://raw.githubusercontent.com/jaegertracing/jaeger-operator/master/deploy/role.yaml
kubectl create -n observability -f https://raw.githubusercontent.com/jaegertracing/jaeger-operator/master/deploy/role_binding.yaml
kubectl create -n observability -f https://raw.githubusercontent.com/jaegertracing/jaeger-operator/master/deploy/operator.yaml
```

> **Note:** that you’ll need to download and customize the cluster_role_binding.yaml if you are using 
> a namespace other than observability. You probably also want to download and customize the operator.yaml, 
> setting the env var WATCH_NAMESPACE to have an empty value, so that it can watch for instances across 
> all namespaces.

```sh
kubectl create -f https://raw.githubusercontent.com/jaegertracing/jaeger-operator/master/deploy/cluster_role.yaml
kubectl create -f https://raw.githubusercontent.com/jaegertracing/jaeger-operator/master/deploy/cluster_role_binding.yaml
```

# Verify Jaeger

```sh
kubectl get deploy jaeger-operator -n observability
kubectl get po,svc -n observability
```

```sh
kubectl apply -n observability -f https://raw.githubusercontent.com/jaegertracing/jaeger-operator/master/examples/business-application-injected-sidecar.yaml
```