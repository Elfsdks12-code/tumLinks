from flask import Flask, render_template
app = Flask(__name__)

SECTIONS = {
    "TUM & Studium" : [
    {"name":"TUMOnline","url":"https://campus.tum.de"},
    {"name":"TUM Moodle","url":"https://www.moodle.tum.de"},
    {"name":"TUM Artemis","url":"https://artemis.cit.tum.de"},
    {"name":"IT-Sicherheit : Scoreboard","url":"https://scoreboard.sec.in.tum.de/"},
    {"name":"GBS-","url":"https://gbs.cm.in.tum.de/"},
    {"name":"GDB - Umbra","url":"https://umbra-db.com/interface/"},
    {"name":"SQL - HyPer","url":"https://hyper-db.de/interface.html#"},
    {"name":"Tutorien","url":"https://tumtutorien.onrender.com/"},
    {"name":"CIT Portal","url":"https://www.cit.tum.de"}
],
    "Nützliches" : [
        {"name":"KVR Termin","url":"https://stadt.muenchen.de/service/info/servicestelle-fur-zuwanderung-und-einburgerung/10339026/#k-contact"},
        {"name":"Boot.dev","url":"https://www.boot.dev/courses"},
        {"name":"Klassische Konzerte","url":"https://auraklassik-munchen.duckdns.org/"},
        {"name":"GitHub","url":"https://github.com/"},
        {"name":"Gebetszeiten","url":"https://namazvakitleri.diyanet.gov.tr/tr-TR/11022/munchen-namaz-vakitleri"},
        {"name":"Massage","url":"https://www.mindoasis.com/de-de/booking"},
        {"name":"Zulip","url":"https://zulip.cit.tum.de/"}
                ]

}

@app.route("/")
def home():
    return render_template("index.html",sections=SECTIONS)

if __name__ == "__main__":
    app.run(debug=True,port=5000)
