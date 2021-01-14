import sys
import os

# POST https://cnt-vrzh-itv02.svc.iptv.rt.ru/api/v2/portal/session_tokens
# send: {"fingerprint":"N1O6paSBkElcapY6Nh5Yz"}
# recv: {"session_id":"016b36e6-567a-11eb-a007-9c1d36dcd53c:1951416:2237006:2","session_state":"demo"}

# url = "https://cnt-vrzh-itv02.svc.iptv.rt.ru/api/v2/portal/channels?limit=30&offset=0&with_epg=true&epg_limit=3"
# session_id = "016b36e6-567a-11eb-a007-9c1b36dcb53c:1951416:2237006:2"
# TE = "Trailers"
# X-Wink-Version = "v2020.12.30.1644"

if __name__ == "__main__":
    print("Wink client")
