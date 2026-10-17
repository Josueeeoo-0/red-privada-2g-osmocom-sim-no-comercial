from Crypto.Cipher import AES
from secrets import token_bytes
from pathlib import Path

def derive_opc(k, op):
    encrypted = AES.new(k, AES.MODE_ECB).encrypt(op)
    return bytes(a ^ b for a, b in zip(encrypted, op))

k = token_bytes(16)
op = token_bytes(16)
opc = derive_opc(k, op)

out = (
    f"K={k.hex().upper()}\n"
    f"OP={op.hex().upper()}\n"
    f"OPC={opc.hex().upper()}\n"
)

Path("credenciales.txt").write_text(out)
Path("credenciales.txt").chmod(0o600)

print("Credenciales generadas y guardadas en credenciales.txt")
print("No publiques ese archivo ni lo compartas.")
