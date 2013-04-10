#!/usr/bin/env python
'''
Minimise CSS by grouping repeated rules together.
'''
from collections import defaultdict
import re, sys

def _parse_css(css):
    '''Takes a string of css and retur a defaultdict in the form rule:selectors'''
    rule_dict = defaultdict(list)
    pattern = re.compile('\s*(.+?)\s*{\s*((?:\s*.+?\s*:\s*.+?;\s*)+?\s*)\s*\}', 
                         flags=re.DOTALL) # Currently doesn't distinguish multiple comma-seperated selectors
    
    for match in pattern.findall(css):
        selector, rules = match
        for rule in rules.split(';')[:-1]: # Exclude blank string at end of rules
            rule_dict[rule + ';'].append(selector)

    return rule_dict

def _flip_dict(rule_dict):
    '''"Flips" the dictionary, mapping collections of selectors to common rules'''
    selector_dict = defaultdict(list)

    for rule, selector in rule_dict.iteritems():
        selector_dict[','.join(selector)].append(rule)

    return selector_dict

def _render_css(flipped_dict):
    '''Renders dict in the form selector:[rules]'''
    return ''.join('{selector}{{{rules}}}'.format(selector=s, rules=''.join(r))
                   for s, r in flipped_dict.iteritems())

def minify(css):
    '''Removes rule repetions in CSS by grouping selectors'''
    return _render_css(_flip_dict(_parse_css(css)))

if __name__ == '__main__':
    print minify(sys.argv[1])
