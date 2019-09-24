# -*- coding: utf-8 -*-
import os
import sys
import xbmc
import xbmcgui
import xbmcplugin
import xbmcaddon
import urllib
import urlparse


addon = xbmcaddon.Addon()
language = addon.getLocalizedString
handle = int(sys.argv[1])
titolo_global = ''
fanart_path = os.path.join(xbmcaddon.Addon().getAddonInfo('path'), 'resources', 'fanart.jpg')
thumb_path = os.path.join(xbmcaddon.Addon().getAddonInfo('path'), 'resources', 'media')




def parameters_string_to_dict(parameters):
    paramDict = dict(urlparse.parse_qsl(parameters[1:]))
    return paramDict


def show_root_menu():
    ''' Show the plugin root menu '''
    liStyle = xbmcgui.ListItem('[B]'+language(32001)+'[/B]')
    liStyle.setArt({ 'thumb': os.path.join(thumb_path, 'camera.jpg'), 'fanart' : fanart_path })
    addDirectoryItem_nodup({"mode": "camera"},liStyle)

    liStyle = xbmcgui.ListItem('[B]'+language(32002)+'[/B]')
    liStyle.setArt({ 'thumb': os.path.join(thumb_path, 'senato.png'), 'fanart' : fanart_path })
    addDirectoryItem_nodup({"mode": "senato"},liStyle)

    liStyle = xbmcgui.ListItem('[B]'+language(32003)+'[/B]')
    liStyle.setArt({ 'thumb': os.path.join(thumb_path, 'tv.png'), 'fanart' : fanart_path })
    addDirectoryItem_nodup({"mode": "tv"},liStyle)

    liStyle = xbmcgui.ListItem('[B]'+language(32004)+'[/B]')
    liStyle.setArt({ 'thumb': os.path.join(thumb_path, 'radio.png'), 'fanart' : fanart_path })
    addDirectoryItem_nodup({"mode": "radio"},liStyle)

    xbmcplugin.endOfDirectory(handle=handle, succeeded=True)


def addDirectoryItem_nodup(parameters, li, title=titolo_global, folder=True):
    url = sys.argv[0] + '?' + urllib.urlencode(parameters, 'utf-8')
    #xbmc.log('LIST------: '+str(url),xbmc.LOGNOTICE)
    return xbmcplugin.addDirectoryItem(handle=handle, url=url, listitem=li, isFolder=folder)


def programmi_camera():
    titolo = 'Camera - Canale Assemblea'
    liStyle = xbmcgui.ListItem(titolo)
    link = 'plugin://plugin.video.youtube/play/?video_id=_pjPv7dS-_w'
    thumb = 'https://webtv.camera.it/system/events/thumbnails/000/014/843/large/AULAXVIIIC.gif'
    liStyle.setArt({ 'thumb': thumb, 'fanart' : fanart_path })
    liStyle.setInfo('video', {})
    liStyle.setProperty('isPlayable', 'true')
    xbmcplugin.addDirectoryItem(handle=handle, url=link, listitem=liStyle, isFolder=False)

    titolo = 'Camera - Canale Satellitare'
    liStyle = xbmcgui.ListItem(titolo)
    link = 'plugin://plugin.video.youtube/play/?video_id=WVjdPb7F4uY'
    thumb = 'https://webtv.camera.it/assets/thumbs/flash_7/2019/EI_20190520_ch4_14419.jpg'
    liStyle.setArt({ 'thumb': thumb, 'fanart' : fanart_path })
    liStyle.setInfo('video', {})
    liStyle.setProperty('isPlayable', 'true')
    xbmcplugin.addDirectoryItem(handle=handle, url=link, listitem=liStyle, isFolder=False)

    xbmcplugin.endOfDirectory(handle=handle, succeeded=True)


def programmi_senato():
    titolo = 'Senato - Web TV 1'
    liStyle = xbmcgui.ListItem(titolo)
    link = 'http://senato-live.morescreens.com/senato-live/ngrp:webtv1_all/playlist.m3u8?DVR'
    thumb = 'http://prd-static-senato.spectar.tv/rev-1544534780/uploads/1/video_thumbnails/upload_318_3763.png'
    liStyle.setArt({ 'thumb': thumb, 'fanart' : fanart_path })
    liStyle.setInfo('video', {})
    liStyle.setProperty('isPlayable', 'true')
    xbmcplugin.addDirectoryItem(handle=handle, url=link, listitem=liStyle, isFolder=False)

    titolo = 'Senato - Web TV 2'
    liStyle = xbmcgui.ListItem(titolo)
    link = 'http://senato-live.morescreens.com/senato-live/ngrp:webtv2_all/playlist.m3u8?DVR'
    thumb = 'http://prd-static-senato.spectar.tv/rev-1544534780/uploads/1/video_thumbnails/upload_471_3766.png'
    liStyle.setArt({ 'thumb': thumb, 'fanart' : fanart_path })
    liStyle.setInfo('video', {})
    liStyle.setProperty('isPlayable', 'true')
    xbmcplugin.addDirectoryItem(handle=handle, url=link, listitem=liStyle, isFolder=False)

    titolo = 'Senato - Web TV 3'
    liStyle = xbmcgui.ListItem(titolo)
    link = 'http://senato-live.morescreens.com/senato-live/ngrp:webtv3_all/playlist.m3u8?DVR'
    thumb = 'http://prd-static-senato.spectar.tv/rev-1544534780/uploads/1/video_thumbnails/upload_390_3769.png'
    liStyle.setArt({ 'thumb': thumb, 'fanart' : fanart_path })
    liStyle.setInfo('video', {})
    liStyle.setProperty('isPlayable', 'true')
    xbmcplugin.addDirectoryItem(handle=handle, url=link, listitem=liStyle, isFolder=False)

    titolo = 'Senato - Web TV 4'
    liStyle = xbmcgui.ListItem(titolo)
    link = 'http://senato-live.morescreens.com/senato-live/ngrp:webtv4_all/playlist.m3u8?DVR'
    thumb = 'http://prd-static-senato.spectar.tv/rev-1544534780/uploads/1/video_thumbnails/upload_569_3772.png'
    liStyle.setArt({ 'thumb': thumb, 'fanart' : fanart_path })
    liStyle.setInfo('video', {})
    liStyle.setProperty('isPlayable', 'true')
    xbmcplugin.addDirectoryItem(handle=handle, url=link, listitem=liStyle, isFolder=False)

    xbmcplugin.endOfDirectory(handle=handle, succeeded=True)


def programmi_tv():

    titolo = 'RaiNews24'
    liStyle = xbmcgui.ListItem(titolo)
    link = 'https://rainews1-live.akamaized.net/hls/live/598326/rainews1/rainews1/playlist.m3u8'
    thumb = 'http://www.rainews.it/dl/components/img/svg/RaiNewsBarra-logo.png'
    liStyle.setArt({ 'thumb': thumb, 'fanart' : fanart_path })
    liStyle.setInfo('video', {})
    liStyle.setProperty('isPlayable', 'true')
    xbmcplugin.addDirectoryItem(handle=handle, url=link, listitem=liStyle, isFolder=False)

    titolo = 'SkyTg24'
    liStyle = xbmcgui.ListItem(titolo)
    link = 'https://skyanywhere3-i.akamaihd.net/hls/live/751544/tg24ta/playlist.m3u8?hdnea=st=1544092653~exp=1608028200~acl=/*~hmac=41be421676ef19322f2982b4e561fba1579a07d7d6cc3898088f6e1758bd9bd1'
    thumb = 'https://pbs.twimg.com/profile_images/1144638925736218624/0Q08kh8-_400x400.png'
    liStyle.setArt({ 'thumb': thumb, 'fanart' : fanart_path })
    liStyle.setInfo('video', {})
    liStyle.setProperty('isPlayable', 'true')
    xbmcplugin.addDirectoryItem(handle=handle, url=link, listitem=liStyle, isFolder=False)

    titolo = 'R.RadicaleTV'
    liStyle = xbmcgui.ListItem(titolo)
    link = 'https://video.radioradicale.it/liverr/padtv2/playlist.m3u8'
    thumb = 'https://media.cdnandroid.com/97/fe/ae/31/imagen-radio-radicale-tv-0big.jpg'
    liStyle.setArt({ 'thumb': thumb, 'fanart' : fanart_path })
    liStyle.setInfo('video', {})
    liStyle.setProperty('isPlayable', 'true')
    xbmcplugin.addDirectoryItem(handle=handle, url=link, listitem=liStyle, isFolder=False)

    titolo = 'La7'
    liStyle = xbmcgui.ListItem(titolo)
    link = 'https://stream.la7.it/out/v1/fe849af8150c4c51889b15dadc717774/index.m3u8'
    thumb = 'https://www.la7.it/img/poster_diretta.jpg'
    liStyle.setArt({ 'thumb': thumb, 'fanart' : fanart_path })
    liStyle.setInfo('video', {})
    liStyle.setProperty('isPlayable', 'true')
    xbmcplugin.addDirectoryItem(handle=handle, url=link, listitem=liStyle, isFolder=False)
    
    titolo = 'Radio24 TV'
    liStyle = xbmcgui.ListItem(titolo)
    link = 'https://radio24-lh.akamaihd.net/i/radio24video_1@379914/master.m3u8'
    thumb = 'http://www.radio24.ilsole24ore.com/images/logo-r24-new.png'
    liStyle.setArt({ 'thumb': thumb, 'fanart' : fanart_path })
    liStyle.setInfo('video', {})
    liStyle.setProperty('isPlayable', 'true')
    xbmcplugin.addDirectoryItem(handle=handle, url=link, listitem=liStyle, isFolder=False)

    xbmcplugin.endOfDirectory(handle=handle, succeeded=True)


def programmi_radio():
    titolo = 'RaiGRParlamento'
    liStyle = xbmcgui.ListItem(titolo)
    link = 'https://grparlamento1-lh.akamaihd.net/i/grparlamento1_1@586839/master.m3u8'
    thumb = 'http://db.radioline.fr/pictures/radio_994f2bf74254de17bb2c096c0cbf9e21/logo200.jpg'
    liStyle.setArt({ 'thumb': thumb, 'fanart' : fanart_path })
    liStyle.setInfo('music', {})
    liStyle.setProperty('isPlayable', 'true')
    xbmcplugin.addDirectoryItem(handle=handle, url=link, listitem=liStyle, isFolder=False)

    titolo = 'RadioRadicale'
    liStyle = xbmcgui.ListItem(titolo)
    link = 'https://live.radioradicale.it/live.mp3'
    thumb = 'https://www.radioradicale.it/sites/all/themes/radioradicale_2014/images/audio-400.png'
    liStyle.setArt({ 'thumb': thumb, 'fanart' : fanart_path })
    liStyle.setInfo('music', {})
    liStyle.setProperty('isPlayable', 'true')
    xbmcplugin.addDirectoryItem(handle=handle, url=link, listitem=liStyle, isFolder=False)

    titolo = 'R.Radicale Camera'
    liStyle = xbmcgui.ListItem(titolo)
    link = 'https://live.radioradicale.it/camera.mp3'
    thumb = 'https://www.radioradicale.it/sites/all/themes/radioradicale_2014/images/audio-400.png'
    liStyle.setArt({ 'thumb': thumb, 'fanart' : fanart_path })
    liStyle.setInfo('music', {})
    liStyle.setProperty('isPlayable', 'true')
    xbmcplugin.addDirectoryItem(handle=handle, url=link, listitem=liStyle, isFolder=False)

    titolo = 'R.Radicale Senato'
    liStyle = xbmcgui.ListItem(titolo)
    link = 'https://live.radioradicale.it/senato.mp3'
    thumb = 'https://www.radioradicale.it/sites/all/themes/radioradicale_2014/images/audio-400.png'
    liStyle.setArt({ 'thumb': thumb, 'fanart' : fanart_path })
    liStyle.setInfo('music', {})
    liStyle.setProperty('isPlayable', 'true')
    xbmcplugin.addDirectoryItem(handle=handle, url=link, listitem=liStyle, isFolder=False)

    titolo = 'RadioPopolare'
    liStyle = xbmcgui.ListItem(titolo)
    link = 'https://livex.radiopopolare.it/radiopop'
    thumb = 'https://www.radiopopolare.it/wp-content/themes/mir-rp/img/testata_logo_rp.png'
    liStyle.setArt({ 'thumb': thumb, 'fanart' : fanart_path })
    liStyle.setInfo('music', {})
    liStyle.setProperty('isPlayable', 'true')
    xbmcplugin.addDirectoryItem(handle=handle, url=link, listitem=liStyle, isFolder=False)
    
    titolo = 'Radio24'
    liStyle = xbmcgui.ListItem(titolo)
    link = 'https://radio24-lh.akamaihd.net/i/radio24_1@99307/master.m3u8'
    thumb = 'http://www.radio24.ilsole24ore.com/images/logo-r24-new.png'
    liStyle.setArt({ 'thumb': thumb, 'fanart' : fanart_path })
    liStyle.setInfo('music', {})
    liStyle.setProperty('isPlayable', 'true')
    xbmcplugin.addDirectoryItem(handle=handle, url=link, listitem=liStyle, isFolder=False)

    xbmcplugin.endOfDirectory(handle=handle, succeeded=True)





# Main
params = parameters_string_to_dict(sys.argv[2])
mode = str(params.get("mode", ""))
titolo_global=str(params.get("titolo", ""))


if mode=="camera":
    programmi_camera()

elif mode=="senato":
    programmi_senato()

elif mode=="tv":
    programmi_tv()

elif mode=="radio":
    programmi_radio()

else:
    show_root_menu()
