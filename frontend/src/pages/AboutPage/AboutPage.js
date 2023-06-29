import React from 'react';

import css from './about.module.css';

const AboutPage = () => {
    return (
        <div className={css.about_wrapper}>
            <div className={css.main_photo}>
                <img src="https://greenville-park.com.ua/inc/uploads/2018/02/Glubochitskaya28_View11.jpg" alt=""/>
            </div>

            <div className={css.about_content}>

                <div className={css.building_technical_view}>
                    <div className={css.technical_block}>
                        <div>
                            <h2>664</h2>
                        </div>
                        <div>
                            <p>Комфортні квартири</p>
                        </div>
                    </div>
                    <div className={css.technical_block}>
                        <div>
                            <h2>25</h2>
                        </div>
                        <div>
                            <p>Просторих поверхів</p>
                        </div>
                    </div>
                    <div className={css.technical_block}>
                        <div>
                            <h2>54</h2>
                        </div>
                        <div>
                            <p>Зручних планування</p>
                        </div>
                    </div>
                    <div className={css.technical_block}>
                        <div>
                            <h2>600</h2>
                        </div>
                        <div>
                            <p>Доступних паркомісць</p>
                        </div>
                    </div>
                    <div className={css.technical_block}>
                        <div>
                            <h2>8000</h2>
                        </div>
                        <div>
                            <p>м2 чудового парку</p>
                        </div>
                    </div>
                </div>
                <div className={css.building_parameters}>
                    <h2>Технічні характеристики</h2>
                    <div className={css.parameters_content}>
                        <div className={css.parameters_image}>
                            <img src="https://greenville-park.com.ua/inc/uploads/2018/02/Glubochitskaya28_View10-2.jpg"
                                 alt=""/>
                        </div>

                        <div className={css.parameters_describe}>
                            <ul>
                                <h3>Технічні характеристики об'єкту:</h3>
                                <li>Кількість поверхів – 25</li>
                                <li>Перші 6 поверхів стилобатна частина</li>
                                <li>Конструкція – залізобетонний монолітний каркас</li>
                                <li>Фасад – керамограніт, навісні вентильовані фасади із утепленням базальтовими
                                    мінераловатними
                                    плитами
                                </li>
                                <li>Стіни міжквартирні – керамічна цегла, 25 см</li>
                                <li>Висота поверху – 330 см, від підлоги до стелі – 295 см</li>
                                <li>Стіни зовнішні – цегляні блоки з утепленням базальтовою ватою</li>
                            </ul>
                        </div>
                    </div>
                    <div className={css.parameters_content}>
                        <div className={css.parameters_describe}>
                            <ul>
                                <h2>Оздоблення квартир:</h2>
                                <li>Вхідні двері – металеві, протиударні із декоративними накладками</li>
                                <li>Вікна та балконні двері – металопластикові 5-камерні із 2-камерним енергозберігаючим
                                    склопакетом
                                </li>
                                <li>Підлога – піщана стяжка 150 мм</li>
                                <li>Санвузли – гідроізоляція підлоги</li>
                            </ul>
                        </div>
                        <div className={css.parameters_image}>
                            <img src="https://greenville-park.com.ua/inc/uploads/2018/02/thumbnail-39.jpg"
                                 alt=""/>
                        </div>

                    </div>
                    <div className={css.parameters_content}>
                        <div className={css.parameters_image}>
                            <img src="https://greenville-park.com.ua/inc/uploads/2018/02/104298_or.jpg"
                                 alt=""/>
                        </div>
                        <div className={css.parameters_describe}>
                            <ul>
                                <h2>Інженерне обладнання:</h2>
                                <li>Ліфти – преміум-класу 5 пасажирських (630 кг) та 1 вантажо-пасажирський (1000 кг) на
                                    кожну секцію
                                </li>
                                <li>Опалення – двотрубна система, індивідуальна котельня Viessmann (Німеччина)</li>
                                <li>Водопостачання – автономні насосні станції LOWARA (Італія) із протипожежною системою
                                </li>
                                <li>Каналізація та опалення – пластикові труби REHAW (Німеччина), труби приховані в
                                    монолітних конструкціях та стяжках
                                </li>
                                <li>Вентиляція – природна витяжна – припливна, потік повітря циркулює через віконні
                                    конструкції та вентиляційні блоки
                                </li>
                                <li>Електроживлення – електропроводка з мідного дроту, установка розподільного щитка
                                </li>
                                <li>Лічильники поквартирні – електролічильник, лічильник гарячої і холодної води і
                                    опалення
                                </li>
                            </ul>
                        </div>

                    </div>

                    <div className={css.parameters_content}>
                        <div className={css.parameters_describe}>
                            <ul>
                                <h2>Оздоблення місць загального користування</h2>
                                <li>Малі архітектурні форми (згідно з проектом)</li>
                                <li>Озеленення – 0,8 га паркової зони</li>
                                <li>Стіни поверхів – керамограніт</li>
                                <li>Підлога сходових маршів та холів – керамічна плитка</li>
                                <li>Двері – відповідно до вимог протипожежної безпеки</li>
                                <li>Стіни – забарвлені водоемульсійними фарбами</li>
                            </ul>
                        </div>
                        <div className={css.parameters_image}>
                            <img src="https://greenville-park.com.ua/inc/uploads/2018/01/IMG_4517.jpg"
                                 alt=""/>
                        </div>

                    </div>
                    <div></div>
                </div>

            </div>
        </div>
    );
};

export {AboutPage};