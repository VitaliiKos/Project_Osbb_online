import React, {useEffect} from 'react';
import {useForm} from "react-hook-form";
import {useDispatch, useSelector} from "react-redux";

import {newsActions} from "../../redux";

const NewsAndEventsForm = () => {
    const {newsForUpdate} = useSelector(state => state.news);
    const dispatch = useDispatch();
    const {register, handleSubmit, reset, setValue} = useForm();


    useEffect(() => {
        if (newsForUpdate) {
            setValue('title', newsForUpdate.title);
            setValue('body', newsForUpdate.body);
        }
    }, [newsForUpdate, setValue])

    const save = async (data) => {
        if (newsForUpdate) {
            const newsId = newsForUpdate.id;
            await dispatch(newsActions.updateNews({newsId, data}));
            dispatch(newsActions.setNewsForUpdate(null));
        }  else {
            await dispatch(newsActions.create({data}));
        }
        reset()
    };

    return (
        <div>
            <h3>NewsAndEventsForm</h3>
            <div>
                <form onSubmit={handleSubmit(save)}>

                    <label><h4>Тема</h4>
                        <input type="text" {...register('title')}/>
                    </label>

                    <label><h4>Опис</h4>
                        <input type="text" {...register('body')}/>
                    </label>
                    <button>{newsForUpdate ? 'Змінити' : 'Створити'}</button>

                </form>
            </div>
        </div>
    );
};

export {NewsAndEventsForm};