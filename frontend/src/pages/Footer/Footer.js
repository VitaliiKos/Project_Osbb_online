import React from 'react';

import css from './footer.module.css';

const Footer = () => {
    return (
        <div className={css.styleFooter}>
            <div className={css.data}>
                <ul>
                    <li>G</li>
                    <li>R</li>
                    <li>E</li>
                    <li>E</li>
                    <li>N</li>
                    <li>V</li>
                    <li>I</li>
                    <li>L</li>
                    <li>L</li>
                    <li>E</li>
                    <li> - </li>
                    <li>P</li>
                    <li>A</li>
                    <li>R</li>
                    <li>K</li>
                </ul>
            </div>
            {/*<div className={`${themeStatus ? css.socialDark : css.social}`}>*/}
            <div className={css.social}>
                <a href={'https://github.com/VitaliiKos'}><i className="fa-brands fa-github"></i></a>
                <a href={'https://www.linkedin.com/in/vitalii-kosyk-836b8917a/'}><i
                    className="fa-brands fa-linkedin"></i></a>
                <a href={'https://t.me/KosykV'}><i className="fa-brands fa-telegram"></i></a>
            </div>
        </div>
    );
};
export {Footer};