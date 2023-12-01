#!/bin/sh
kubectl apply -f tweet-trend-new/namespace.yaml
kubectl apply -f tweet-trend-new/secret.yaml
kubectl apply -f tweet-trend-new/deployment.yaml
kubectl apply -f tweet-trend-new/service.yaml