import requests
import json

API_KEY     = "r+wMsjs/s0ebWiv6TPfo9ACzPiRGBPGiOCUCwsSJsjkFIliNZXlKaGJHY2lPaUpTVXpJMU5pSXNJbXRwWkNJNkluTnBaeTB5TURJeExUQTNMVEV6VkRFNE9qVXhPalE1V2lJc0luUjVjQ0k2SWtwWFZDSjkuZXlKaGRXUWlPaUpTYjJKc2IzaEpiblJsY201aGJDSXNJbWx6Y3lJNklrTnNiM1ZrUVhWMGFHVnVkR2xqWVhScGIyNVRaWEoyYVdObElpd2lZbUZ6WlVGd2FVdGxlU0k2SW5JcmQwMXphbk12Y3pCbFlsZHBkalpVVUdadk9VRkRlbEJwVWtkQ1VFZHBUME5WUTNkelUwcHphbXRHU1d4cFRpSXNJbTkzYm1WeVNXUWlPaUkzTnpZNU1qVTFOVEFpTENKbGVIQWlPakUzTnpneE16VXlOelFzSW1saGRDSTZNVGMzT0RFek1UWTNOQ3dpYm1KbUlqb3hOemM0TVRNeE5qYzBmUS5Jc0dPNzhudlExbkw2QzEyRjFaUXZvTzFXOHhKb2N3TDh0aVVrTlFPUVpndU4xYXVkOUo1bWlHX0cwWHYzS0xPcWUzZ0VHRWtIcEl0eXhPMVhVNjY3eEJTQTZoNXJCSTRHakhLeVpsNmVsOWZTZzlTaWdDb3hnYWdtVjdGdE9lS3Roci1ZQW1rLXUwX3FqOFRQTW5NeTl1ZWFzQWZkM0RtbW0zcldJWU5FQlpKdVFMOE5ydmVMU1UzbmJ3bXI3QlNiTzRHVWMyUHpHVWtNMm1EcGRvME1hcnBUcXFJajM4Mk9xeGtXNy14eFh4dGd0cnlkZ2dTQk01OVlTUUVHNEVwUTQtZ2RhT0Q1ZE5rSFR1bnpPNG1IaVhBN3Y2RzRzbXd5WTZmTmhyRjRaMnlfYTNpaFVLSlNvXzVKak9HM3h0WHNvcEQxWjVjaUhJWHpxdC1KeFNmdEE="
UNIVERSE_ID = "10007549036"

DATASTORES = [
    ("LevelOrdered_v1",    "global", "export_LevelOrdered_v1.json"),
    ("PlaytimeOrdered_v1", "global", "export_PlaytimeOrdered_v1.json"),
]

headers = {"x-api-key": API_KEY}

for store_name, scope, output_file in DATASTORES:
    print(f"\n=== EXPORT: {store_name} (scope={scope}) ===")
    url      = f"https://apis.roblox.com/ordered-data-stores/v1/universes/{UNIVERSE_ID}/orderedDataStores/{store_name}/scopes/{scope}/entries"
    params   = {"max_page_size": 100, "order_by": "desc"}
    exported = []

    while True:
        response = requests.get(url, headers=headers, params=params)
        print(f"Status: {response.status_code}")

        data    = response.json()
        entries = data.get("entries", [])

        for entry in entries:
            exported.append({"key": entry["id"], "value": entry["value"]})
            print(f"  [EXPORT] key={entry['id']} | value={entry['value']}")

        next_token = data.get("nextPageToken")
        if not next_token:
            break
        params["page_token"] = next_token

    with open(output_file, "w") as f:
        json.dump(exported, f, indent=2)

    print(f"  [DONE] {len(exported)} entries -> {output_file}")

print("\n=== SEMUA EXPORT SELESAI ===")

