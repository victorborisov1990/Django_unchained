from django.shortcuts import render
from django.http import HttpResponse


# Создайте пару представлений в вашем первом приложении:
# — главная
# — о себе.
# Внутри каждого представления должна быть переменная html — многострочный текст с HTML-вёрсткой и данными о вашем первом
# Django-сайте и о вас. Сохраняйте в логи данные о посещении страниц.

def start(request):
    return HttpResponse('''
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Document</title>
                <link rel="stylesheet" href="/css/style.css">
            </head>
            <body>
                <nav class="navigation">
                    <a class="navigation__link" href="/">Главная</a>
                    <a class="navigation__link" href="/about/">Обо мне</a>
                </nav>
                <h1 class = "title">Моя первая html страница</h1>
                <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Totam laudantium sed voluptate necessitatibus? Fugit ipsam dolorem doloribus ratione laborum ut aliquam delectus quos. Provident corrupti placeat quibusdam, temporibus fugit corporis quis officia beatae maiores cum sapiente veritatis minus, voluptatem excepturi, quisquam dolore. Esse numquam hic natus rerum nisi ipsum earum suscipit neque distinctio voluptatem adipisci optio sit, quibusdam saepe veritatis doloremque enim incidunt in eligendi corrupti quo illum qui! Magnam rerum ea, sint veniam, quo voluptatum iusto ab, earum eaque velit accusantium aliquid! Harum maiores rerum mollitia sequi? Necessitatibus iusto nihil, quam asperiores esse recusandae. Eaque alias facere fugiat voluptates.</p>
                <h2 class="title2">Заголовок 2 уровня</h2>
                <p class = "text">Lorem ipsum dolor sit amet, consectetur adipisicing elit. Deserunt amet laborum ducimus laudantium nostrum aspernatur quibusdam accusamus repellat cupiditate architecto nisi, enim saepe ipsum nobis iste assumenda consequuntur maiores libero sit autem quisquam cumque dolor exercitationem? Ratione, hic vitae labore adipisci, ipsa saepe ut facere beatae fugit tempora voluptas veritatis?</p>
                <p class = "text">Lorem ipsum dolor sit amet, consectetur adipisicing elit. Deserunt amet laborum ducimus laudantium nostrum aspernatur quibusdam accusamus repellat cupiditate architecto nisi, enim saepe ipsum nobis iste assumenda consequuntur maiores libero sit autem quisquam cumque dolor exercitationem? Ratione, hic vitae labore adipisci, ipsa saepe ut facere beatae fugit tempora voluptas veritatis?</p>
                <p class = "text">Lorem ipsum dolor sit amet, consectetur adipisicing elit. Deserunt amet laborum ducimus laudantium nostrum aspernatur quibusdam accusamus repellat cupiditate architecto nisi, enim saepe ipsum nobis iste assumenda consequuntur maiores libero sit autem quisquam cumque dolor exercitationem? Ratione, hic vitae labore adipisci, ipsa saepe ut facere beatae fugit tempora voluptas veritatis?</p>
            
            </body>
            </html> class = "text"
    ''')


def about(request):
    return HttpResponse('''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>About</title>
        </head>
        <body>
            <nav>
                <a href="/">Главная</a>
                <a href="/about/">Обо мне</a>
            </nav>
            <h1>Обо мне</h1>
            <p>Lorem ipsum dolor sit amet consectetur, adipisicing elit. Quos id rem ipsam tempora ad alias dignissimos 
            porro beatae ab, accusantium dolorem rerum itaque, in quaerat atque quibusdam dolores corrupti ullam enim adipisci laudantium eos ducimus. Ratione modi architecto consequuntur dolore enim adipisci praesentium repudiandae nisi ad optio beatae corporis delectus placeat quae, sit, eum consequatur rem, provident ab at impedit! At, distinctio nihil officiis enim nesciunt rem aliquid eos, nostrum repudiandae in qui sapiente, ad possimus. Voluptates minus harum, eligendi voluptatibus eum, magni non id saepe sapiente quia quam unde possimus perspiciatis rem dolorum deserunt in quaerat molestiae officiis temporibus vero atque facere? Exercitationem laboriosam odio neque temporibus repudiandae magni minus eligendi natus quis aliquid dolorum accusamus aut officiis placeat, numquam quasi enim sapiente dicta ipsum delectus? Atque suscipit sapiente, voluptate id architecto minima, ratione officiis nihil repellendus ipsum iste quia libero et. Officiis labore obcaecati, ullam nostrum aliquid in?</p>
        </body>
        </html>
        ''')