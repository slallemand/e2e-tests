import requests
import argparse

def test_health_check(server):
    url = f"{server}/"
    print(f"Running E2E Test: Checking service health at {url}...")
    
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            print("✅ Service is healthy")
        else:
            print(f"❌ Service is down (HTTP {response.status_code})")
            exit(1)
    except requests.exceptions.RequestException as e:
        print(f"❌ Request failed: {e}")
        exit(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="E2E Health Check Test")
    parser.add_argument("--server", type=str, default="http://localhost:8080", help="Server URL (default: http://localhost:8080)")
    args = parser.parse_args()

    test_health_check(args.server)
