from jose import jwe
import json

def format_public_key_to_pem(public_key):
    pem_header = "-----BEGIN PUBLIC KEY-----"
    pem_footer = "-----END PUBLIC KEY-----"

    chunks = [public_key[i:i+64] for i in range(0, len(public_key), 64)]
    pem_content = "\n".join(chunks)
    pem_key = f"{pem_header}\n{pem_content}\n{pem_footer}"

    return pem_key

data = {
    "cardNumber": "4111111111111122",
    "expiryMonth": "03",
    "expiryYear": "36",
    "securityCode": "737",
    "holderName": "John Doe",
    "holderReference": "Amgd Wafik"
}

publick_key = "MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA3kOM8fTXa7oMdYxGCa9u8Z6ym2Ldczt2x7kAmHKV9jT8YG7PaGxv4E5nRjZnT9OU0fZZAGUGng1RDrRaCFwcZpOD5m56sG1LaYQ8dkaxSG2M1BynLeK9XRiZEmx1JhD0Pk4mm5sIFIg3Oa486CWMVrjgCpsF1VIgT7yGoNOk8tdOqPZ206ATXd+5BxArQ3aup9ziD0nsk66CRchXVCgF7Gc/ySEsc+B3GhF4qqFSvZbAJ4hG1uc1/8G2XbKoJIdpgc4QavnvtADATJBmqyHio70ds76gQJAMs8uMpgN9FOqYqj5XSEX9K/WbHQBnqjBoprZPngq8hzHukbx8XhqrfQIDAQAB"

# '...' should be the public key 
publicKey = format_public_key_to_pem(publick_key)

jsonData = json.dumps(data).encode('utf-8')
# {"cardNumber":"4111111111111111","expiryMonth":"03","expiryYear":"30","securityCode":"737","holderName":"John Doe","holderReference":"customer123"}

encryptedCardData = jwe.encrypt(plaintext=jsonData, algorithm='RSA-OAEP-256', encryption='A256CBC-HS512', key=publicKey)
# eyJhbGciOiJSU0EtT0FFUC0yNTYiLCJlbmMiOiJBMjU2R0NNIn0...

print(encryptedCardData.decode('utf-8'))

