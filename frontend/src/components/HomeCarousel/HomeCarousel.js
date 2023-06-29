import React from "react";
import {Carousel} from "react-responsive-carousel";

import css from './homeCarousel.module.css';
const HomeCarousel = () => {
    const slideNumberStyle = {
        fontSize: "20px",
        fontWeight: "bold"
    };
    return (
        <div className={css.carousel_image_presentation}>
            <Carousel
                autoPlay
                width="70vw"
                height="300px"
                radius="10px"
                slideNumber={true}
                slideNumberStyle={slideNumberStyle}
                dots={true}
                showIndicators={true}
                showStatus={true}
                showArrows={true}
                infiniteLoop={true}
                thumbnails={true}
                thumbnailWidth="100px"
            >
                <div>
                    <img
                        src="https://inventure.com.ua/img/thumb.990.660/upload/pic2022-1H/GHK-Kiev-2022.jpg"
                        alt=""
                    />
                </div>
                <div>
                    <img
                        src="https://inventure.com.ua/upload/user/3909/22409.jpg"
                        alt=""
                    />
                </div>
                <div>
                    <img
                        src="https://greenville-park.com.ua/inc/uploads/2018/02/Glybochicka_28_Fasad_BB_daylight_View018__.jpg"
                        alt=""
                    />
                </div>
                <div>
                    <img
                        src="https://inventure.com.ua/img/thumb.990.660/upload/pic2022-1H/GHK-Kiev-2022.jpg"
                        alt=""
                    />
                </div>
                <div>
                    <img
                        src="https://greenville-park.com.ua/inc/uploads/2018/02/Glubochitskaya28_View10-1.jpg"
                        alt=""
                    />
                </div>
                <div>
                    <img
                        src="https://inventure.com.ua/img/thumb.990.660/upload/pic2022-1H/GHK-Kiev-2022.jpg"
                        alt=""
                    />
                </div>
                <div>
                    <img
                        src="https://greenville-park.com.ua/inc/uploads/2018/02/Glubochitskaya28_View10-1.jpg"
                        alt=""
                    />
                </div>
            </Carousel>
        </div>
    );
};
export {HomeCarousel};
