<template>
  <div class="new">
    <!-- Comments Form -->
    <div class="container">
      <div class="card my-5">
        <h5 class="card-header">新建博客</h5>
        <div class="card-body">
          <!-- <form> -->
          <div class="form-group">
            <input
              v-model="blogTitle"
              class="form-control my-2"
              type="text"
              placeholder="标题"
              maxlength="20"
            />

            <div class="tag">
              <!-- TODO:添加标签选择 -->
              <el-tag
                :key="tag"
                v-for="tag in dynamicTags"
                closable
                :disable-transitions="false"
                @close="handleClose(tag)"
              >{{tag}}</el-tag>
              <el-input
                class="input-new-tag"
                v-if="inputVisible"
                v-model="inputValue"
                ref="saveTagInput"
                size="small"
                maxlength="20"
                @keyup.enter.native="handleInputConfirm"
                @blur="handleInputConfirm"
              ></el-input>
              <el-button v-else class="button-new-tag" size="small" @click="showInput">+ 标签</el-button>
            </div>
            <textarea class="form-control" rows="13" v-model="blogText"></textarea>
            <label for="blogImg">上传图片（可选）：
            <input type="file" name="blogImg" id="blogImg" @change=getFile($event)>

            </label>
          </div>
          <!-- 数据要提交到store中 -->
          <button type="submit" class="btn btn-primary" v-on:click.prevent="addBlog">提交</button>
          <!-- </form> -->
        </div>
      </div>
    </div>
  </div>
</template>

<script>
let formData = new FormData();

export default {
  name: "New",
  data() {
    return {
      blogTitle: "",
      blogText: "",
      dynamicTags: [],
      inputVisible: false,
      inputValue: "",
      blogImg: '',
    };
  },
  components: {},
  methods: {
    addBlog() {
      formData.append('title', this.blogTitle);
      formData.append('content', this.blogText);
      formData.append('tags', JSON.stringify(this.dynamicTags));
      formData.append('imgUrl', this.blogImg);
      // console.log(formData);
      this.$store.dispatch("addBlog", formData);
    },
    getFile(event) {
      this.blogImg = event.target.files[0];
      // console.log(this.blogImg);
      
    },

    handleClose(tag) {
      this.dynamicTags.splice(this.dynamicTags.indexOf(tag), 1);
    },

    showInput() {
      this.inputVisible = true;
      this.$nextTick((_) => {
        var that = _;
        console.log(that);
        this.$refs.saveTagInput.$refs.input.focus();
      });
    },

    handleInputConfirm() {
      let inputValue = this.inputValue;
      if (inputValue) {
        this.dynamicTags.push(inputValue);
      }
      this.inputVisible = false;
      this.inputValue = "";
    },
  },
};
</script>

<style lang="scss" scoped>
.el-tag + .el-tag {
  margin-left: 10px;
}
.button-new-tag {
  margin-left: 10px;
  height: 32px;
  line-height: 30px;
  padding-top: 0;
  padding-bottom: 0;
}
.input-new-tag {
  width: 90px;
  margin-left: 10px;
  vertical-align: bottom;
}
</style>