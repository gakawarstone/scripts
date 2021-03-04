# встреча с леной в начале первого дня она стестняется и ты просто проходишь а может и не просто проходишь посмотрим что пидумаю
# мини игра про баскетболл с системой прокачки попадание идет на рандом игра в 33 просто спрайты и бекграунд кольца прописать
# систему игры

label day_1:
    $ day_time()
    $ persistent.sprite_time = "day"
    scene bus with dissolve2
    th "Так стоп а где это я..."
    th "Что я здесь делаю"
    th "О а я тут не один"
    show rei_cas at left with dissolve
    show dio_pio at right with dissolve
    show gen_pio at cleft with dissolve
    show gws_cas at cright with dissolve
    show m6g_jac with dissolve
    th "Тут уже знакомые мне Ваня Рома Гена Рустам и Данил"
    scene bus with dissolve2
    show lis_pio at left with dissolve
    show aml_pio at right with dissolve
    show evl_cas at cleft with dissolve
    show kat_cas at cright with dissolve
    show eva_pio with dissolve
    th "И еще"
    scene bus with dissolve2
    show kri_cas at left with dissolve
    show lik_cas at right with dissolve
    show mas_cas at cleft with dissolve
    show rit_cas at cright with dissolve
    show ant_cas with dissolve
    th "И еще"
    scene bus with dissolve2
    show dan_pio at left with dissolve
    show kol_pio at right with dissolve
    show ily_cas at cleft with dissolve
    show lid_cas at cright with dissolve
    show tim_pio with dissolve
    th "Но кто это такие и почему они тоже здесь"
    th "Что случилось с нашей ГЕЙ ПАРТИ откуда здесь они"
    th "Зачем они здесь..."
    "*Какой-то шум"
    "Ребята разговаривают между собой"
    th "Чувствую себя каким то изгоем"
    th "Если вы понимаете о чем я"
    show unblink
    scene bg ext_camp_entrance_day with dissolve2
    show sl normal pioneer with dissolve2
    "..."
    th "Опа а нас тут видимо ждали может какую ЦЕРЕМОНИЮ организуют"
    sl "Привет ребята.{w} Как доехали?{w} Мы вас тут уже всем лагерем заждались"
    lis "Интерестно очень интерестно я так понимаю мы все не то чтобы планировали здесь оказаться"
    th "Действительно поддерживаю я вот вообще не помню как здесь оказался"
    th "Конечно это можно списать на Альцгеймер но все я ж не настолько"
    th "Ну хотябы про то что я отправляюсь в лагерь я бы не забыл"
    sl "Чтож я понимаю что вы все хотите друг с другом пообщатся но давайте сейчас решим организациионные момент"
    sl "А после я вам обещаю что вам будет предоставлена возможность познокомится"
    sl "Мы ожидали что вы приедете пораньше так что нам стоит немного поторопится"
    sl "Вы все пройдемте в лагерь"
    scene bg ext_square_day with dissolve2
    show sl normal pioneer at left
    show mt normal panama pioneer at right
    mt "Благодарю Славя за то что привела их сюда"
    mt "Так вот вижу вы уже приехали теперь мы можем начать"
    mt "Сейчас мы распроделяемся по домикам"
    mt "Все слушайте внимательно повторять небуду"
    mt "Но перед этим проведем перекличку вдруг кто потеялся"
    mt "Начнем..."

    mt "Амелия"
    show aml_pio with dissolve2
    aml "Здесь"
    th "Оу перекличка как интерестно... Могли бы ченить поинтерестнее придумать"

    mt "Антон"
    hide aml_pio with dissolve
    show ant_cas with dissolve2
    ant "Здесь"
    mt "Так так почему не в форме?"
    ant "А ну это..."
    mt "Понятно..."
    mt "Слушайте сюда внимательно все кто не в форме"
    mt "Форму вы сможете получить в около склада встретитесь там с нашим физруком он вам и выдаст форму"
    mt "Я думаю все все поняли к складу после переклички вас проведет Славя"
    sl "Хорошо Ольга Дмитриевна"


    mt "Денис"
    hide ant_cas with dissolve
    show dan_pio with dissolve2
    dan "Здесь"

    mt "Ева"
    hide dan_pio with dissolve
    show eva_pio with dissolve2
    eva "Здесь"
    th "Кого то она мне напоминает 365 раз ее я где-то видел"
    th "Может просто похожа..."

    mt "Эвелина"
    hide eva_pio with dissolve
    show evl_cas with dissolve2
    evl "Здесь"
    mt "Иди к Славе сейчас после переклички пойдете за формой"

    mt "Ваня"
    hide evl_cas with dissolve
    show gws_cas with dissolve2
    gws "Здесь"
    mt "Опять же форма понял?"
    gws "А да понял"
    mt "И допей уже свою колу и выкинь ее у нас тут такое непринято"
    gws "Ладно"

    mt "Рустам"
    hide gws_cas with dissolve
    show dio_pio with dissolve2
    dio "Здесь"
    mt "Думаю ты понял ты тоже идешь за формой"

    mt "Гена"
    hide dio_pio with dissolve
    show gen_pio with dissolve2
    gen "Здесь"

    mt "Илья"
    hide gen_pio with dissolve
    show ily_cas with dissolve2
    ily "Здесь"
    mt "Форма я думаю уже все поняли но я все таки повторю"

    mt "Катя"
    hide ily_cas with dissolve
    show kat_cas with dissolve2
    kat "Здесь"
    mt "Форма"

    mt "Коля"
    hide kat_cas with dissolve
    show kol_pio with dissolve2
    kol "Здесь"

    mt "Кристина"
    hide kol_pio with dissolve
    show kri_cas with dissolve2
    kri "Здесь"
    mt "Как же много вас безформенных ну да ладно"

    mt "ЛидА"
    hide kri_cas with dissolve
    show lid_cas with dissolve2
    lid "Здесь"

    mt "Лиза"
    hide lid_cas with dissolve
    show lis_pio with dissolve2
    lis "Здесь"

    mt "Лика"
    hide lis_pio with dissolve
    show lik_cas with dissolve2
    lik "Здесь"

    mt "Рома"
    hide lik_cas with dissolve
    show m6g_jac with dissolve2
    m6g "Здесь"

    mt "Маша"
    hide m6g_jac with dissolve
    show mas_cas with dissolve2
    mas "Здесь"

    mt "Моника"
    hide mas_cas with dissolve
    show mnc_pio with dissolve2
    mnc "Здесь"

    mt "Рита"
    hide dan_pio with dissolve
    show rit_cas with dissolve2
    rit "Здесь"

    mt "Тимур"
    hide rit_cas with dissolve
    show tim_pio with dissolve2
    tim "Здесь"

    mt "Вот мы и закончили перекличку"
    mt "Да многовато вас здесь"

    th ""


    mt "Э старый состав к вам тут пополнение из далеких великих степей процветающей союзной республики Казахстан"
    mt "Вас дохуя а меня нихуя поэтому я решила тут так сказат суеты навести"
#    mt "Корочи салаги слушайте внимательно я заебалась тут за вашими шароебами следить поэтому епта"
#    mt "Теперь меня будет три Ахуели? И правильно сделали"
#    mt "Я вам представляю двух новых вожатых Анечку и Нику и сандалевы паганцы чтоб не доебывали их"

#    рита предет попозжя вместе с новыми вожатыми
#    show lisa_std at left
#    show lika_std at right
#    show mnc_std
#    show an
#    так как вас стало очень даже многовато теперь у нас будет еще одна вожатая Анечка
#    Анечка у нас немного ебнутая и решила косплеить какаши ну никто ей этого не запретит так что все норм
#    ебаный насвай чета вас дохуя как бы вас сука познокомить а ну давайте поиграем в часы окей ну да окей катя с элей сьебутся походу игры помогать в столовку
#    ебаные вы прокрастиноторы сцука вы должны лять щаписаться на какую нибуь хуйню и ходить туда а не шароебится блять здесь это вам не летний лагерь это гулак блять
#    это наш физрук Павел Николаевич если хочешь стать как жатара то тебе к нему
#    на пидар обходной лист иди обхади
