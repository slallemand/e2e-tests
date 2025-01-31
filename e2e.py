import requests
import argparse

def test_endpoints(server, endpoints):
    print(f"Running E2E Tests on {server}...")

    for endpoint in endpoints:
        url = f"{server}{endpoint}"
        print(f"🔍 Testing {url}...")
        try:
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                print(f"✅ {endpoint} is healthy")
            else:
                print(f"❌ {endpoint} failed (HTTP {response.status_code})")
                exit(1)
        except requests.exceptions.RequestException as e:
            print(f"❌ {endpoint} request failed: {e}")
            exit(1)

    print("🎉 All tests passed!")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="E2E Health Check Test")
    parser.add_argument("--server", type=str, default="http://simple-app.my-app.svc.cluster.local:8080", help="Server URL (default: http://simple-app.my-app.svc.cluster.local:8080)")
    args = parser.parse_args()

    # List of endpoints to check
    endpoints = ["/", "/api/hello", "/toto"]

    test_endpoints(args.server, endpoints)
