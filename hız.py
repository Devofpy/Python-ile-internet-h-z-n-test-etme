#kütüphaneyi kurmak için
pip install speedtest-cli

from speedtest import Speedtest
st = Speedtest()

print(`indirme hızı : `, st.download()/1000000, `Mbps`)
print(`yükleme hızı : `, st.upload()/1000000, `Mbps`)

