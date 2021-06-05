import webbrowser
import folium

p = [ ]
for k in range(1):
    a=input("위도, 경도:")
    c=input("팝업을 입력하시오:")
    d=input("색깔을 입력하시오:")
    b= a.split(',')
    for i in range(2):
        b[i] = float(b[i])
    b.append(c)
    b.append(d)
    
    p.append(b)

print(p)

cent1=0
cent2=0
for i in range(len(p)):
    cent1 = cent1+p[i][0]
    cent2 = cent2+p[i][1]
cent1= cent1/len(p)
cent2=cent2/len(p)
parking_map = folium.Map(location = [cent1, cent2],
                             zoom_start=15)

print(cent1, cent2)

for i in range(len(p)):


    folium.Marker([p[i][0], p[i][1]],
                  icon = folium.Icon(color=p[i][3],icon='info-sign'),
                  popup = p[i][2]).add_to(parking_map)

parking_map.save('index.html')
webbrowser.open('index.html')

