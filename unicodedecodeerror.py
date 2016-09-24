def decode_me_maybe(encoded, encodings):
    for encoding in encodings:
        try:
            decoded = encoded.decode(encoding)
        except UnicodeDecodeError:
            pass
        else:
            return decoded
    else:
        raise UnicodeDecodeError

 encoded = get_encoded_string_from_unreliable_source()
 encodings = ('ascii', 'iso-8859-1',
              'utf-32', 'utf-16', 'utf-8')
 decoded = decode_me_maybe(encoded, encodings)
