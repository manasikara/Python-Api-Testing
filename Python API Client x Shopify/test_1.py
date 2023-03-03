# learning source --> https://youtu.be/E39a7kQfjSg

import requests
import creds    

def create_session():
    s = requests.Session()
    s.headers.update({
        "X-Shopify-Access-Token": creds.token,
        "Content-Type": "application/json"
    })
    return s


def main():
    sess = create_session()
    resp = sess.get(creds.url + "/admin/api/2021-07/products.json?limit=10")
    print(resp.json())
    
if __name__ == '__main__':
    main()    
    
    
    
    
    # to be continued - stuck at fricking error "AttributeError: module 'creds' has no attribute 'token'"
    
    # 1:52