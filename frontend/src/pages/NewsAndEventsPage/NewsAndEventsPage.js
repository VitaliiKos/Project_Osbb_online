import React, {useEffect} from 'react';
import {useDispatch, useSelector} from "react-redux";
import {useSearchParams} from "react-router-dom";

import {newsActions} from "../../redux";
import {NewsAndEvents, NewsAndEventsForm, Polls} from "../../components";
import css from './css.module.css';

const NewsAndEventsPage = () => {
    const {news, prevPage, NexPage} = useSelector(state => state.news);

    const dispatch = useDispatch();
    const [query, setQuery] = useSearchParams({'page': '1'});

    useEffect(() => {
        dispatch(newsActions.getAll({'page': query.get('page')}))
    }, [query])

    return (<div className={css.wrapper}>
            <div className={css.newsWrapper}>
                <div className={css.newsForm}>
                    <NewsAndEventsForm/>
                </div>
                {news && news.map(item => <NewsAndEvents key={item.id} item={item}/>)}
            </div>

            <div className={css.pollWrapper}>
                <Polls/>
            </div>

        </div>);
};

export {NewsAndEventsPage};