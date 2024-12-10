import requests
import sys

def main()-> None:
    if len(sys.argv) < 2:
        print(f"Missing command-line argument")
        sys.exit(1)
    else:
        try:
            bitcoin: float = float(sys.argv[1])
        except ValueError:
            print(f"Command-line argument is not a number")
            sys.exit(1)
        else:
            try:
                response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").json()
                bitcoin_price = response["bpi"]["USD"]["rate_float"]
            except requests.RequestException:
                sys.exit(1)
            else:
                total = round(bitcoin_price * bitcoin, 4)
                print("${:,}".format(total))
                sys.exit(0)
if __name__ =="__main__":
    main()