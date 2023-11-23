import qrcode

def create_qr(data, filename):
    qr = qrcode.make(data)
    qr.save(filename)

data = input("character you want to encode:  ")
filename = input("file name:  ")
filename = f'{filename}.png'

if __name__ == "__main__":
    create_qr(data, filename)
    print("QR Downloaded!")