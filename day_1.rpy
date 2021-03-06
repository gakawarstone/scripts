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
    show aml_pio with dissolve
    aml "Здесь"
    th "Оу перекличка как интерестно... Могли бы ченить поинтерестнее придумать"
    show aml_pio at go_out_right

    mt "Антон"
    hide aml_pio
    show ant_cas with dissolve
    ant "Здесь"
    mt "Так так почему не в форме?"
    ant "А ну это..."
    mt "Понятно..."
    mt "Слушайте сюда внимательно все кто не в форме"
    mt "Форму вы сможете получить в около склада встретитесь там с нашим физруком он вам и выдаст форму"
    mt "Я думаю все все поняли к складу после переклички вас проведет Славя"
    sl "Хорошо Ольга Дмитриевна"
    show ant_cas at go_out_left


    mt "Денис"
    hide ant_cas
    show dan_pio with dissolve
    dan "Здесь"
    show dan_pio at go_out_right

    mt "Ева"
    hide dan_pio
    show eva_pio with dissolve
    eva "Здесь"
    th "Кого то она мне напоминает 365 раз ее я где-то видел"
    th "Может просто похожа..."
    show eva_pio at go_out_right

    mt "Эвелина"
    hide eva_pio
    show evl_cas with dissolve
    evl "Здесь"
    mt "Иди к Славе сейчас после переклички пойдете за формой"
    show evl_cas at go_out_left

    mt "Ваня"
    hide evl_cas
    show gws_cas with dissolve
    gws "Здесь"
    mt "Опять же форма понял?"
    gws "А да понял"
    mt "И допей уже свою колу и выкинь ее у нас тут такое непринято"
    gws "Ладно"
    show gws_cas at go_out_left

    mt "Рустам"
    hide gws_cas
    show dio_pio with dissolve
    dio "Здесь"
    mt "Думаю ты понял ты тоже идешь за формой"
    show dio_pio at go_out_left

    mt "Гена"
    hide dio_pio
    show gen_pio with dissolve
    gen "Здесь"
    show gen_pio at go_out_right

    mt "Илья"
    hide gen_pio
    show ily_cas with dissolve
    ily "Здесь"
    mt "Форма я думаю уже все поняли но я все таки повторю"
    show ily_cas at go_out_left

    mt "Катя"
    hide ily_cas
    show kat_cas with dissolve
    kat "Здесь"
    mt "Форма"
    show kat_cas at go_out_left

    mt "Коля"
    hide kat_cas
    show kol_pio with dissolve
    kol "Здесь"
    show kol_pio at go_out_right

    mt "Кристина"
    hide kol_pio
    show kri_cas with dissolve
    kri "Здесь"
    mt "Как же много вас безформенных ну да ладно"
    show kri_cas at go_out_left

    mt "ЛидА"
    hide kri_cas
    show lid_cas with dissolve
    lid "Здесь"
    show lid_cas at go_out_left

    mt "Лиза"
    hide lid_cas
    show lis_pio with dissolve
    lis "Здесь"
    show lis_pio at go_out_right

    mt "Лика"
    hide lis_pio
    show lik_cas with dissolve
    lik "Здесь"
    show lik_cas at go_out_left

    mt "Рома"
    hide lik_cas
    show m6g_jac with dissolve
    m6g "Здесь"
    mt "Снимай свою куртку тебе че холодно?"
    m6g "Окей ясьненько"
    show m6g_jac at go_out_right

    mt "Маша"
    hide m6g_jac
    show mas_cas with dissolve
    mas "Здесь"
    show mas_cas at go_out_left

    mt "Моника"
    hide mas_cas
    show mnc_pio with dissolve
    mnc "Здесь"
    show mnc_pio at go_out_right

    mt "Рита"
    hide dan_pio
    show rit_cas with dissolve
    rit "Здесь"
    show rit_cas at go_out_left

    mt "Тимур"
    hide rit_cas
    show tim_pio with dissolve
    tim "Здесь"
    show tim_pio at go_out_right
    mt "Вот мы и закончили перекличку"
    mt "Да многовато вас здесь"
    th "Ля наконец то..."
    th "Может мы уже начнем что нибудь интересное..."
    th "А Альцгеймер чуть не забыл мы же за формой идем"
    th "И че мы стоим..."
    mt "Что ж те ко за формой идите за Славей"
    sl "Ребята пойдемте за мной"
    show sl normal pioneer at go_out_left
    jump go_for_uniform


label go_for_uniform:
    scene ext_road_day with dissolve2
    scene admin_day with dissolve2
    show fmn_spt
    th "..."
    fmn "Я так понимаю они все за формой"
    sl "Да"
    fmn "Многовато их ну да ладно"



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
