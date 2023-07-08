import {createAsyncThunk, createSlice} from "@reduxjs/toolkit";
import {pollService} from "../../services";

const initialState = {
    polls: [],
    pollForUpdate:null,
    loading: false,
    errors: null,

}

const getAll = createAsyncThunk(
    'pollSlice/getAll',
    async ({page}, thunkAPI) => {
        try {
            const {data} = await pollService.getAll(page);
            return data;
        } catch (e) {
            return thunkAPI.rejectWithValue(e.response.data);
        }
    }
)

const getById = createAsyncThunk(
    'pollSlice/getById',
    async ({id}, thunkAPI) => {
        try {
            await pollService.getById(id);
        } catch (e) {
            return thunkAPI.rejectWithValue(e.response.data);
        }
    }
)

const createPoll = createAsyncThunk(
    'pollSlice/createPoll',
    async ({poll}, thunkAPI) => {
        try {
            await pollService.add(poll)
            thunkAPI.dispatch(getAll({'page': 1}));
        } catch (e) {
            return thunkAPI.rejectWithValue(e.response.data);
        }
    }
)

const updatePoll = createAsyncThunk(
    'pollSlice/updatePoll',
    async ({pollId, poll}, thunkAPI) => {
        try {
            await pollService.updateById(pollId, poll);
        } catch (e) {
            return thunkAPI.rejectWithValue(e.response.data);
        }
    }
)

const deletePoll = createAsyncThunk(
    'pollSlice/deletePoll',
    async ({id}, thunkAPI) => {
        try {
            await pollService.deleteById(id);
            thunkAPI.dispatch(getAll({'page': 1}));
        } catch (e) {
            return thunkAPI.rejectWithValue(e.response.data);
        }
    }
)

const makeVote = createAsyncThunk(
    'pollSlice/makeVote',
    async ({id, data}, thunkAPI) => {
        try {
            await pollService.vote(id, data);
            thunkAPI.dispatch(getAll({'page': 1}));

        } catch (e) {
            return thunkAPI.rejectWithValue(e.response.data);
        }
    }
)

const pollSlice = createSlice({
    name: 'pollSlice',
    initialState,
    reducers: {
        setPollForUpdate: (state, action) => {
            state.pollForUpdate = action.payload;
        },
    },
    extraReducers: builder => builder
        .addCase(getAll.fulfilled, (state, action) => {
            state.loading = false;
            const {data} = action.payload;
            state.polls = data;

        })
        .addCase(getAll.rejected, (state, action) => {
            state.loading = false;
            state.errors = action.payload;

        })
        .addCase(getAll.pending, (state) => {
            state.loading = true;
        })
});

const {reducer: pollReducer, actions:{setPollForUpdate}} = pollSlice;

const pollActions = {
    getAll,
    createPoll,
    getById,
    updatePoll,
    deletePoll,
    makeVote,
    setPollForUpdate,
}

export {pollActions, pollReducer};