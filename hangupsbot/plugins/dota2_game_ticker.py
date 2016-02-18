# Dota 2 Match Info
#
# Fetches latest live and upcoming Dota2 games on request, outputs game info into chat
#
# Author: Alex Muench <ammuench@gmail.com>

import sys

from gosu_gamers import gg_match

import plugins

"""
Prints live, upcoming and recent matches of all dota games
"""

def gamelist(bot, event, *args):
    ggms = gg_match.Dota2MatchScraper()

    subcommand = "".join(args)
    #print("This is the subcommand: " + subcommand)

    #return list of all available commands
    if subcommand == "" or subcommand == " " or subcommand == "help":
        list = "<b><u>Available Commands:</u></b>\n"
        list += "<b>all</b>: Show all live games, and nearest upcoming games\n"
        list += "<b>live</b>: Show all live games\n"
        list += "<b>upcoming</b>: Show 5 upcoming games"
        yield from bot.coro_send_message(event.conv, _(list))

    #return live and upcoming games
    elif subcommand == "all":
        match_printout = '<b><u>Live:</u></b>\n'
        for match in ggms.find_live_matches():
            match_printout += match.team1 + " (" + match.team1_bet + ")\nvs\n" + match.team2 + " (" + match.team2_bet + ")\n\n"
            #DEPRECATED: Gosugamers no longer provides the name of the tournament correctly, this may be changed in the future  
            #match_printout += "<i>League: " +  match.tournament + "</i>\n\n"
        
        match_printout += "\n"
        match_printout += "<b><u>Upcoming:</u></b>\n"

        for match in ggms.find_upcoming_matches()[0:6]:
            match_printout += match.team1 + " (" + match.team1_bet + ")\nvs\n" + match.team2 + " (" + match.team2_bet + ")\n"
            #DEPRECATED: Gosugamers no longer provides the name of the tournament correctly, this may be changed in the future  
            #match_printout += "<i>League: " +  match.tournament + "</i>\n"
            match_printout += "<i>Match Starts in : " +  match.live_in + "</i>\n\n"

        yield from bot.coro_send_message(event.conv, _(match_printout))

    #return live games only
    elif subcommand == "live":
        match_printout = '<b><u>Live:</u></b>\n'
        for match in ggms.find_live_matches():
            match_printout += match.team1 + " (" + match.team1_bet + ")\nvs\n" + match.team2 + " (" + match.team2_bet + ")\n\n"
            #DEPRECATED: Gosugamers no longer provides the name of the tournament correctly, this may be changed in the future  
            #match_printout += "<i>League: " +  match.tournament + "</i>\n\n"

        yield from bot.coro_send_message(event.conv, _(match_printout))

    #return upcoming games only
    elif subcommand == "upcoming":
        match_printout = "<b><u>Upcoming:</u></b>\n"
        for match in ggms.find_upcoming_matches()[0:6]:
            match_printout += match.team1 + " (" + match.team1_bet + ")\nvs\n" + match.team2 + " (" + match.team2_bet + ")\n"
            #DEPRECATED: Gosugamers no longer provides the name of the tournament correctly, this may be changed in the future  
            #match_printout += "<i>League: " +  match.tournament + "</i>\n"
            match_printout += "<i>Match Starts in : " +  match.live_in + "</i>\n\n"

        yield from bot.coro_send_message(event.conv, _(match_printout))

    #catchall for wrong commands
    else:
        yield from bot.coro_send_message(event.conv, _("I'm sorry, I don't know that command yet"))



def _initialise(bot):
    plugins.register_user_command(["gamelist"])
