import {createAsyncThunk, createSlice} from "@reduxjs/toolkit";
import {newsEventsService} from "../../services";

const initialState = {
    news: [],
    errors: null,
    loading: null,
    prevPage: null,
    nextPage: null,
    total_pages: null,
    total_items: null,

    current_news: null,
    newsForUpdate: null,
}
const getAll = createAsyncThunk(
    'newsSlice/getAll',
    async ({page}, thunkAPI) => {
        try {
            const {data} = await newsEventsService.getAll(page);
            return data
        } catch (e) {
            return thunkAPI.rejectWithValue(e.response.data)
        }
    }
)

const create = createAsyncThunk(
    'newsSlice/create',
    async ({data}, thunkAPI) => {
        try {
            await newsEventsService.add(data)
            thunkAPI.dispatch(getAll({'page': 1}))
        } catch (e) {
            return thunkAPI.rejectWithValue(e.response.data)
        }
    }
)

const deleteNews = createAsyncThunk(
    'newsSlice/deleteNews',
    async ({id}, thunkAPI) => {
        try {
            await newsEventsService.deleteById(id)
        } catch (e) {
            return thunkAPI.rejectWithValue(e.response.data)
        }
    }
)

const updateNews = createAsyncThunk(
    'newsSlice/updateNews',
    async ({newsId, data}, thunkAPI) => {
        try {
            await newsEventsService.updateById(newsId, data)
        } catch (e) {
            return thunkAPI.rejectWithValue(e.response.data)
        }
    }
)

const newsEventsSlice = createSlice({
    name: 'newsSlice',
    initialState,
    reducers: {
        setNewsForUpdate: (state, action) => {
            state.newsForUpdate = action.payload.item
        }
    },
    extraReducers: builder => builder
        .addCase(getAll.fulfilled, (state, action) => {
            state.loading = false;
            const {data} = action.payload
            state.news = data

        })
        .addCase(getAll.rejected, (state, action) => {
            state.loading = false;
            state.errors = action.payload
        })
        .addCase(getAll.pending, (state) => {
            state.loading = true;
        })
})

const {reducer: newsReducer, actions: {setNewsForUpdate}} = newsEventsSlice;
const newsActions = {
    getAll,
    create,
    deleteNews,
    updateNews,
    setNewsForUpdate,
}

export {newsReducer, newsActions}