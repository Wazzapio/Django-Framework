from django.shortcuts import render

import json
import os
MODULE_DIR = os.path.dirname(__file__)
# Create your views here.

def index(request):
    context = {
        'title': 'geekshop',
    }
    return render(request, 'mainapp/index.html', context)


def products(request):
    file_path = os.path.join(MODULE_DIR, 'fixtures/prods.json')
    context = {
        'title': 'geekshop - Продукты',
    }
    context['products'] = json.load(open(file_path, encoding='utf-8'))
        # 'products': [
        #
        #     {'name': 'Худи черного цвета с монограммами adidas Originals',
        #      'price': '6 090,00 руб.',
        #      'text': 'Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни.',
        #      'picture': 'vendor/img/products/Adidas-hoodie.png',
        #      },
        #
        #     {'name': 'Синяя куртка The North Face',
        #      'price': '23 725,00 руб.',
        #      'text': 'Гладкая ткань. Водонепроницаемое покрытие. Легкий и теплый пуховый наполнитель.',
        #      'picture': 'vendor/img/products/Blue-jacket-The-North-Face.png',
        #      },
        #
        #     {'name': 'Коричневый спортивный oversized-топ ASOS DESIGN',
        #      'price': '3 390,00 руб.',
        #      'text': 'Материал с плюшевой текстурой. Удобный и мягкий.',
        #      'picture': 'vendor/img/products/Brown-sports-oversized-top-ASOS-DESIGN.png',
        #      },
        #
        #     {'name': 'Черный рюкзак Nike Heritage',
        #      'price': '2 340,00 руб.',
        #      'text': 'Плотная ткань. Легкий материал.',
        #      'picture': 'vendor/img/products/Black-Nike-Heritage-backpack.png',
        #      },
        #
        #     {'name': 'Черные туфли на платформе с 3 парами люверсов Dr Martens 1461 Bex',
        #      'price': '13 590,00 руб.',
        #      'text': 'Гладкий кожаный верх. Натуральный материал.',
        #      'picture': 'vendor/img/products/Black-Dr-Martens-shoes.png',
        #      },
        #
        #     {'name': 'Темно-синие широкие строгие брюки ASOS DESIGN',
        #      'price': '2 890,00 руб.',
        #      'text': 'Легкая эластичная ткань сирсакер Фактурная ткань.',
        #      'picture': 'vendor/img/products/Dark-blue-wide-leg-ASOs-DESIGN-trousers.png',
        #      },
        # ]

    return render(request, 'mainapp/products.html', context)
