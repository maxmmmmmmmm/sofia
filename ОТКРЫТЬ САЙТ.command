#!/bin/bash
# Двойной клик — поднимает локальный сервер и открывает сайт.
# Закрыть окно Терминала = остановить сервер.
cd "$(dirname "$0")"
PORT=4321

# Адрес машины в локальной сети — по нему сайт открывается с телефона
LAN=""
for i in $(networksetup -listallhardwareports 2>/dev/null | awk '/Device/{print $2}'); do
  ip=$(ipconfig getifaddr "$i" 2>/dev/null)
  if [ -n "$ip" ]; then LAN="$ip"; break; fi
done

echo ""
echo "  На этом компьютере:  http://localhost:$PORT"
if [ -n "$LAN" ]; then
  echo "  С телефона:          http://$LAN:$PORT"
  echo ""
  echo "  Телефон должен быть в той же сети Wi-Fi, что и компьютер."
else
  echo "  С телефона: адрес не определён — нет подключения к сети."
fi
echo ""
echo "  Мобильная версия:    http://localhost:$PORT/mobile.html"
echo ""
echo "  Остановить — закрыть это окно или Ctrl+C."
echo ""

( sleep 1; open "http://localhost:$PORT" ) &
python3 -m http.server $PORT
