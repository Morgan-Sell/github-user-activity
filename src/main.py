import requests

from src.config import GITHUB_API_URL


def main():

    username = input("Which GitHub user's activity would you like to see? ")
    full_url = f"{GITHUB_API_URL}{username}"

    response = requests.get(full_url)

    if response.status_code == 200:

        user_data = response.json()

        # Print out some user information
        print(f"Username: {user_data['login']}")
        print(f"Name: {user_data.get('name', 'N/A')}")
        print(f"Company: {user_data.get('company', 'N/A')}")
        print(f"Location: {user_data.get('location', 'N/A')}")
        print(f"Public Repos: {user_data['public_repos']}")
        print(f"Followers: {user_data['followers']}")
        print(f"Following: {user_data['following']}")
        print(f"Profile URL: {user_data['html_url']}")

    else:
        print(
            f"Error: Unable to fetch data for user '{username}'. Status code: {response.status_code}"
        )


if __name__ == "__main__":
    main()
