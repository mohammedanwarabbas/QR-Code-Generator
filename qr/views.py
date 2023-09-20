from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def generateqr(request):
    if request.method=='POST':
        '''Old version starts'''
        # qrtext = request.POST['qrtext'] 
        # import qrcode  
        # # generating a QR code using the make() function  
        # qr_img = qrcode.make(qrtext)  
        # # saving the image file  
        # qr_img.save("static/qr-img.jpg")
        '''Old version ends'''
        
        '''New version starts'''
        qrtext = request.POST['qrtext']
        box_size = request.POST['bs']
        border = request.POST['b']
        fc = request.POST['fc']
        bc = request.POST['bc']
        if box_size=="":
            box_size=6
        if border=="":
            border=5
        if fc=="":
            fc="black"
        if bc=="":
            bc="white"
        print(qrtext,box_size,border,fc,bc)
        import qrcode  
        qr = qrcode.QRCode(
        version=12,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=box_size,
        border=border
        )
        qr.add_data(qrtext)
        qr_img = qr.make_image(fill_color=fc, back_color=bc)
        qr_img.save("static/qr-img.jpg")
        '''new version ends'''
        
        return render(request, 'qr.html')  

