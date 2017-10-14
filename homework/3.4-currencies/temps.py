import chardet
import osa


def average_temp(temps_list):
    print(temps_list)
    aver_temp = sum(temps_list) / len(temps_list)
    print('Average temp:', round(aver_temp), 'F')
    
    client = osa.Client('http://www.webservicex.net/ConvertTemperature.asmx?WSDL')
    res = client.service.ConvertTemp(Temperature=aver_temp,
                                     FromUnit='degreeFahrenheit',
                                     ToUnit='degreeCelsius')
    print('Average temp:', round(res), 'C')
    

def main(file):
    with open(file, 'rb') as f:
        data = f.read()
        result = chardet.detect(data)
        text = data.decode(result['encoding'])
        temp = text.split(' F')
        temps_list = [int(temp[x].strip()) for x in range(len(temp))
                      if temp[x]]
        average_temp(temps_list)


if __name__ == '__main__':
    main('temps.txt')
