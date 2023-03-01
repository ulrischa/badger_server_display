import badger2040w
from phew import server, connect_to_wifi

badger = badger2040w.Badger2040W()

wifi_ssid= "XXX"
wifi_pw = "XXX"

padding_x = 20
padding_y = 20

def print_badger_txt(txt):
    badger.set_pen(15)
    badger.clear()
    badger.set_pen(0)
    badger.set_font("bitmap8")
    badger.text(txt, padding_x, padding_y, scale=2, wordwrap=badger2040w.WIDTH-2*padding_y)
    badger.update()


def bootstrap():
    ip = connect_to_wifi(wifi_ssid, wifi_pw)
    if ip is not None:
        print_badger_txt("Send me something at: http://"+ip+"/t /my_text_here \n")
        badger.led(255)

        
@server.route("/t/<incoming_text>", methods=["GET"])
def send_text(request, incoming_text):
    incoming_text = server.urldecode(incoming_text)
    print_badger_txt(incoming_text)
    return incoming_text, 200


@server.catchall()
def catchall(request):
  return "Not found", 404


bootstrap()
server.run()
