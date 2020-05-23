import pylast
import json
from datetime import datetime, timedelta  


API_KEY = 'YOUR_API_KEY'
API_SECRET='YOUR_SERET_KEY'


username = "YOUR_LASTFM_USERNAME"
password_hash = pylast.md5("YOUR_LASTFM_PASSWORD")

network = pylast.LastFMNetwork(api_key=API_KEY, api_secret=API_SECRET,
                               username=username, password_hash=password_hash)






# how long to pause between consecutive API requests
# pause_duration = 0.2






#GeoMethods
geo_top_tracks=network.get_geo_top_tracks('Spain')
for play in geo_top_tracks:
    print(f" {play.item} and playcount is {play.weight}")

geo_top_tracks=network.get_geo_top_artists('Spain')
for play in geo_top_tracks:
    print(f" {play.item}")





#Album methods:
album=network.get_album("Doja cat", "Amala")
album_info=album.get_url()
album_id=album.get_mbid()




#User Methods
user = network.get_user(username)
user_top_artists = user.get_top_artists(period="12month")

user_loved_tracks = user.get_loved_tracks()
user_top_artists=user.get_top_artists()
user_top_albums=user.get_top_albums()
user_recent_tracks=user.get_recent_tracks()
user_now_playing= user.get_now_playing()
# user_artist_tracks=user.get_artist_tracks("Doja cat")
user_track_scrobbles=user.get_track_scrobbles("Doja cat", "Say so")
user_top_tracks=user.get_top_tracks()
today=datetime.today()

d = today-timedelta(days =2)
from_to=d.strftime("%d/%m/%Y")
to_date=today.strftime("%d/%m/%Y")

user_weekly_album_chart=user.get_weekly_album_charts(from_date=from_to,to_date=to_date)

user_weekly_chart_list=user.get_weekly_chart_dates()

user_weekly_artist_chart=user.get_weekly_artist_charts()

user_weekly_track_chart=user.get_weekly_track_charts()
user_info=network.get_user('harish647')

if user_now_playing==None:
    print("your are not playing anything now on connected service")

for hot in user_top_artists:
     print(f"{hot.item.name} ,the total listened {hot.weight}")

for hot in user_loved_tracks:
    ts = int(hot.timestamp)
    print(f"{hot.track} ,datetime :{datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')}")

for hot in user_top_albums:
     print(f"{hot.item} , {hot.weight}")

for hot in user_recent_tracks:
     print(f"{hot.track} ,album is {hot.album},at  {hot.playback_date}")

for hot in user_track_scrobbles:
    print(hot.track)
    
print(user_track_scrobbles.track)

     print(f"{hot.track} ,album is {hot.album},at  {hot.playback_date}")

print(len(user_track_scrobbles))
for hot in user_track_scrobbles[0]:
	# mul_string=
    print(f"{str(hot)},scrobbles {len(user_track_scrobbles)}times")
    break

for hot in user_top_tracks:
     print(f"{hot.item} , {hot.weight}")

for hot in user_weekly_album_chart:
     print(f"{hot.item} , {hot.weight}")

for hot in user_weekly_artist_chart:
     print(f"{hot.item} , {hot.weight}")
for hot in user_weekly_track_chart:
     print(f"{hot.item} , {hot.weight}")








#Artist Methods
top_artists = network.get_top_artists(limit=100)
for hot in top_artists:
    print(f"{hot.item.name} ,the total listeners {hot.weight}")

artist_similar=network.get_artist("Doja cat")
artist_similar=artist_similar.get_similar()
for hot in artist_similar:
    print(f"{hot.item.name}")

artist=network.get_artist("Doja cat")
hot=artist.get_top_albums()
hot1=artist.get_top_tracks()
hot3=artist.get_correction()
hot4=artist.get_wiki_content()
if hot4==None:
    print("There is no wiki content of this artist")

hot6=artist.get_bio_summary()
hot7=artist.get_mbid()
hot8=artist.get_tags()
hot9=artist.get_url()
# hot10=artist.get_userplaycount()
hot11=artist.get_cover_image()
hot12=artist.get_bio_published_date()

if len(hot8)==0:
    print("there are no tags")
for play in hot:
    print(f"Top Album of Doja Cat  are {play.item} and playcount is {play.weight}")

for play in hot1:
    print(f"Top Track of Doja Cat  are {play.item}and playcount is {play.weight}")





