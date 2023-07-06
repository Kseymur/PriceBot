my_file = open('/Users/kseniiamurasheva/PycharmProjects/PriceBot/yolov5/data/custom.yaml','w+')
my_file.write('train: /Users/kseniiamurasheva/PycharmProjects/PriceBot/images/train/ \nval: /Users/kseniiamurasheva/PycharmProjects/PriceBot/images/val/ \ntest: /Users/kseniiamurasheva/PycharmProjects/PriceBot/images/test/ \n# number of classes \nnc: 2 \n# class names \nnames: ["price", "description"]')


my_file.readlines()