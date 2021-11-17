from django.shortcuts import render


# Create your views here.

def index(request):
    context = {
        'title': 'geekshop',
    }
    return render(request, 'index.html', context)


def products(request):
    context = {
        'title': 'geekshop - Продукты',
        'products': [

            {'name': 'Худи черного цвета с монограммами adidas Originals',
             'price': '6 090,00 руб.',
             'text': 'Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни.',
             'picture': '/static/vendor/img/products/Adidas-hoodie.png',
             },

            {'name': 'Синяя куртка The North Face',
             'price': '23 725,00 руб.',
             'text': 'Гладкая ткань. Водонепроницаемое покрытие. Легкий и теплый пуховый наполнитель.',
             'picture': '/static/vendor/img/products/Blue-jacket-The-North-Face.png',
             },

            {'name': 'Коричневый спортивный oversized-топ ASOS DESIGN',
             'price': '3 390,00 руб.',
             'text': 'Материал с плюшевой текстурой. Удобный и мягкий.',
             'picture': '/static/vendor/img/products/Brown-sports-oversized-top-ASOS-DESIGN.png',
             },

            {'name': 'Черный рюкзак Nike Heritage',
             'price': '2 340,00 руб.',
             'text': 'Плотная ткань. Легкий материал.',
             'picture': '/static/vendor/img/products/Black-Nike-Heritage-backpack.png',
             },

            {'name': 'Черные туфли на платформе с 3 парами люверсов Dr Martens 1461 Bex',
             'price': '13 590,00 руб.',
             'text': 'Гладкий кожаный верх. Натуральный материал.',
             'picture': '/static/vendor/img/products/Black-Dr-Martens-shoes.png',
             },

            {'name': 'Темно-синие широкие строгие брюки ASOS DESIGN',
             'price': '2 890,00 руб.',
             'text': 'Легкая эластичная ткань сирсакер Фактурная ткань.',
             'picture': '/static/vendor/img/products/Dark-blue-wide-leg-ASOs-DESIGN-trousers.png',
             },
        ]
    }
    return render(request, 'products.html', context)
