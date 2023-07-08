import React from 'react';

import css from './homePage.module.css'
import {HomeCarousel} from "../../components";
import 'react-responsive-carousel/lib/styles/carousel.min.css';

const HomePage = () => {
    return (
        <div className={css.wrapperHomepage}>
            <div className={css.description}>
                <>
                    <div className={css.presentation}>
                        <div className={css.presentation_title}>
                            <h2>Greenville Park</h2>
                            <h3><a href="https://greenville-park.com.ua/">greenville-park</a></h3>
                        </div>
                        <div className={css.presentation_image}>
                            <img src="https://greenville-park.com.ua/inc/uploads/2018/02/Glubochitskaya28_View12.jpg"
                                 alt=""/>
                        </div>
                    </div>

                    <div className={css.presentation_slide}>
                        <HomeCarousel/>
                    </div>
                </>

                <div className={css.parameters_content}>
                    <div className={css.parameters_image}>
                        <img src="https://greenville-park.com.ua/inc/uploads/2021/07/0004-min-scaled.jpg"
                             alt=""/>
                    </div>

                    <div className={css.parameters_describe}>
                        <div>
                            <h4>Все для комфортного життя</h4>
                        </div>
                        <div>
                            <p>
                                Сучасна краса – це стиль без зайвих деталей. Запарковані двори, колони, кондиціонери на
                                фасаді будинку – це не про красу, а значить – не про Greenville Park.

                                <br/>
                                Ми доповнили сучасну архітектуру Києва житловим комплексом у сіро-зеленій кольоровій
                                гаммі
                                та помістили його на шестиповерховий стилобат.

                                <br/>
                                Для спокою та безпеки мешканців на вході у будинок поставили охорону та зробили доступ
                                лише
                                за індивідуальною картковою системою. Територія будинку закрита як від сторонніх, так і
                                для
                                в’їзду машин, щоб у дворі було спокійно і дорослим, і дітям.

                                <br/>
                                Усе необхідне – поряд: супермаркет у будинку, ресторани, кав’ярні, тренажерний зал. Але
                                головне відбувається, як тільки заходиш у хол: просторий і світлий, з дизайнерським
                                ремонтом, великою кількістю світла та зелені.

                                <br/>
                                Перший поверх площею понад 1000 м.кв. облаштований для комфорту мешканців: є лаунж- та
                                бізнес-зона, ігрова дитяча кімната, де можна залишити малих в безпеці та приділити час
                                собі,
                                колясочна, щоб безпечно паркувати дитячі возики, і також лапомийка для песиків є.

                                <br/>
                                Навіть запах в будинку особливий: ретельно підібраний, із нотами свіжості та димкою
                                теплоти
                                і затишку. Оце краса!
                            </p>
                        </div>
                    </div>
                </div>

                <div className={css.parameters_content}>
                    <div className={css.parameters_describe}>
                        <div>
                            <h4>Сучасний і функціональний дизайн</h4>
                        </div>
                        <div>
                            <p>
                                Форма будинку – це розгорнута книга: пиши власну історію та споглядай Поділ як на
                                долоні.

                                <br/>
                                Цегляні блоки зовнішніх стін мають відмінну морозостійкість, тому навіть в
                                найнеприємнішу зиму не змерзнете. І опалення на максимум не потрібне. В будинку
                                автономне опалення котельнею Viessmann (Німеччина) та автономні насосні станції
                                італійського виробника Lowara.

                                <br/>
                                Зовнішні стіни комплексу водонепроникні та довговічні, тож з роками погодні умови не
                                зіпсують красивий фасад. Кондиціонери його теж не завісять, бо для них спеціально
                                відведено приховані ніші на кожному поверсі.

                                <br/>
                                Всередині будинку є один вантажний та п’ять пасажирських ліфтів. Щоб не витрачати час на
                                даремне очікування.

                            </p>
                        </div>
                    </div>
                    <div className={css.parameters_image}>
                        <img
                            src="https://greenville-park.com.ua/inc/uploads/2018/02/Glubochitskaya28_View10-615x690.jpg"
                            alt=""/>
                    </div>
                </div>

                <div className={css.parameters_content}>
                    <div className={css.parameters_image}>
                        <img src="https://greenville-park.com.ua/inc/uploads/2020/11/6-min.jpg" alt=""/>
                    </div>

                    <div className={css.parameters_describe}>
                        <div>
                            <h4>Все, що треба для сім’ї з дітьми</h4>
                        </div>
                        <div>
                            <p>
                                Сучасні майданчики, гойдалки та гірки, простір для гри, знайомство із першими друзями –
                                продумано все, щоб малюкам було добре вдома.

                                <br/>
                                На першому поверсі є ігрові кімнати, де молоді привіті няні гратимуться та навчатимуть
                                дітлахів.

                                <br/>
                                Двір закритий і безпечний – щоб малі грали, а батьки не хвилювалися. Є простір, щоб
                                кидати м’яча і вчитися кататися на велосипеді.

                                <br/>
                                А на терасі продумана дитяча зона: поки малюк захоплено грається, є час попити каву і
                                спланувати день.
                            </p>
                        </div>
                    </div>
                </div>

                <div className={css.parameters_content}>

                    <div className={css.parameters_describe}>
                        <div>
                            <h4>Дбаємо, щоб ЖК був красивим і через 50 років</h4>
                        </div>
                        <div>
                            <p>
                                Тому створили власну управлінську компанію, працівники якої завжди на зв’язку:
                                спілкуються з вами у чатах мешканців, обговорюють важливі питання: від благоустрою
                                будинку до допомоги з пошуком загубленої сережки.

                                <br/>
                                Адміністратор слідкує за порядком і виконує прохання мешканців.

                                <br/>
                                Охорона слідкує за безпекою і не пускає сторонніх у комплекс.

                                <br/>
                                Прибиральники тримають комплекс у чистоті і красі.

                                <br/>
                                І, звісно, у нас є споглядач краси, який за всім цим слідкує.

                                <br/>
                                Наша команда працює щодня, щоб ЖК Greenville Park був красивим сьогодні, завтра і через
                                50 років
                            </p>
                        </div>
                    </div>

                    <div className={css.parameters_image}>
                        <img src="https://greenville-park.com.ua/inc/uploads/2021/11/0020-min-scaled.jpg" alt=""/>
                    </div>

                </div>


            </div>
        </div>
    );
};

export {HomePage};