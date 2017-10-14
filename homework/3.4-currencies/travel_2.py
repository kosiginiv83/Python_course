import osa
import sys


def length_convert(mi):
    client = osa.Client('http://www.webservicex.net/length.asmx?WSDL')
    res = client.service.ChangeLengthUnit(LengthValue=mi,
                                     fromLengthUnit='Miles',
                                     toLengthUnit='Kilometers')
    print('Total:', round(res, 2), 'km')


def main(file):
    length_list = []
    with open(file) as f:
        for line in f:
            item = line.split()
            length_list.append(item[1])
    print(length_list)
    length_list = [float(length_list[x].replace(',', '')) for x in
                   range(len(length_list))]
    print(length_list)
    mi = sum(length_list)
    print('Total:', mi, 'mi')
    length_convert(mi)


if __name__ == '__main__':
    file = sys.argv[1]
    main(file)
