#! /usr/bin/env python

import argparse
import xerox
from code import emojiCodeDict

def emoji_search(args):

    words = args['query']
    to_print = u''
    
    for search in words:
        exact_search = ':' + search + ':'
        exact = False
        for key in emojiCodeDict.keys():
            if exact_search == key:
                if to_print:
                    to_print = to_print + ' ' + emojiCodeDict[key]
                else:
                    to_print =  emojiCodeDict[key]
                exact = True
                break
        if exact:
            continue 
        for key in emojiCodeDict.keys():
            if search in key: 
                if to_print:
                    to_print = to_print + ' ' + emojiCodeDict[key]
                else:
                    to_print =  emojiCodeDict[key]
                break

    print to_print 
    if args['copy']:
        xerox.copy(to_print)

def list_all_emoji(copy=False):
  
    to_copy = '' 
    for word in emojiCodeDict.keys():
        print word + ' ' + emojiCodeDict[word] 
        to_copy = to_copy + word + ' ' + emojiCodeDict[word] + '\n'        
    if copy:
        xerox.copy(to_copy)

def dump_all_emoji(copy=False):
  
    to_print = '' 
    for word in emojiCodeDict.keys():
        to_print = to_print + ' ' + emojiCodeDict[word] 
    print to_print
    
    if copy:
       xerox.copy(to_print)

def get_parser():
    parser = argparse.ArgumentParser(description='Command line emoji search.')
    parser.add_argument('query', metavar='QUERY', type=str, nargs='*',
            help='the emoji to search for')
    parser.add_argument('-c','--copy', help='copy result to the clipboard.', default=False, dest='copy', action='store_true')
    parser.add_argument('-l','--list', help='list all of the available emoji.', default=False, dest='list', action='store_true')
    parser.add_argument('-a','--all', help='dump all of the available emoji.', default=False, dest='all', action='store_true')
    return parser

def command_line_runner():
    parser = get_parser()
    args = vars(parser.parse_args())
    if not args['query'] and not args['list'] and not args['all']:
        parser.print_help()
        return
    if ['query']:
        emoji_search(args)
    
    if args['list']:
        list_all_emoji(args['copy'])
    
    if args['all']:
        dump_all_emoji(args['copy'])

if __name__ == '__main__':
    command_line_runner()
