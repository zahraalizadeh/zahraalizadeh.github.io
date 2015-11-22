__author__ = 'alizadeh'
def huffman(probs):
    """Return Huffman codewords for the given probability distribution."""
    nodes = [[x] for x in range(len(probs))]
    merged_probs = probs[:]
    while len(nodes) > 1:
        # find two least probable nodes:
        (mn, idx) = min_argmin(merged_probs)
        merged_probs[idx] = INF
        (mn2, idx2) = min_argmin(merged_probs)
        # merge them:
        merged_probs[idx] = mn + mn2;
        del merged_probs[idx2]
        nodes[idx] = [nodes[idx], nodes[idx2]]
        del nodes[idx2]

    # Recursive navigation of tree of nested lists to construct codes
    def huffman_helper(cur_code, nodes, codes):
        if len(nodes) == 1:
            symbol = nodes[0]
            codes[symbol] = cur_code
        else:
            huffman_helper(cur_code + '0', nodes[0], codes)
            huffman_helper(cur_code + '1', nodes[1], codes)
    codes = ['' for x in range(len(probs))]
    huffman_helper('', nodes[0], codes)
    return codes
def symbol_code_expected_length(probs, codes):
    return sum(x*len(y) for (x,y) in zip(probs, codes))

def Hbits(probs):
    """Entropy of discrete distribution, measured in bits."""
    from math import log
    return sum(-x*log(x, 2) for x in probs if x !=0)

def main():
    import sys
    if len(sys.argv) < 2:
        print __doc__
        sys.exit(1)
    probs = map(float, sys.argv[1:])
    Z = sum(probs)
    probs = [x/Z for x in probs]
    codes = huffman(probs)
    Lbar = symbol_code_expected_length(probs, codes)
    print 'Codewords:'
    print '----------'
    for cc in codes:
        print cc
    print '----------'
    print 'Expected length: %g bits/symbol' % Lbar
    print 'Entropy of dist: %g bits/symbol' % Hbits(probs)

if __name__ == "__main__":
    main()


