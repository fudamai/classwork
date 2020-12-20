<template>
  <div class="update">
    <!-- Comments Form -->
    <div class="container">
      <div class="card my-5">
        <h5 class="card-header">编辑博客</h5>
        <div class="card-body">
          <!-- <form> -->
          <div class="form-group">
            <input
              v-model="blog.title"
              class="form-control my-2"
              type="text"
              placeholder="标题"
              maxlength="20"
            />

            <div class="tag">
              <!-- TODO:添加标签选择 -->
              <el-tag
                :key="tag"
                v-for="tag in blog.tags"
                closable
                :disable-transitions="false"
                @close="handleClose(tag)"
                >{{ tag }}</el-tag
              >
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
              <el-button
                v-else
                class="button-new-tag"
                size="small"
                @click="showInput"
                >+ 标签</el-button
              >
            </div>
            <textarea
              class="form-control"
              rows="13"
              v-model="blog.content"
            ></textarea>
            <label for="blogImg"
              >上传图片（可选）：
              <input
                type="file"
                name="blogImg"
                id="blogImg"
                @change="getFile($event)"
              />
            </label>
            <div v-if="blog.imgUrl">
              <img
                class="img-fluid rounded old-img"
                v-bind:src="blog.imgUrl"
                alt="图片"
              />
            </div>
            <div v-else>无图片</div>
          </div>
          <!-- 数据要提交到store中 -->
          <button
            type="submit"
            class="btn btn-primary"
            v-on:click.prevent="updateBlog"
          >
            提交
          </button>
          <!-- </form> -->
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters } from "vuex";

let formData = new FormData();

export default {
  name: "Update",
  data() {
    return {
      blog: "",
      dynamicTags: [],
      inputVisible: false,
      inputValue: "",
      blogImg: "",
    };
  },
  components: {},
  computed: {
    ...mapGetters(["blogs"]),
  },
  created() {
    this.blogFill();
  },
  methods: {
    updateBlog() {
      formData.append("title", this.blog.title);
      formData.append("content", this.blog.content);
      formData.append("tags", JSON.stringify(this.blog.tags));
      if (this.blogImg) {
        formData.append("imgUrl", this.blogImg);
      }
      console.log(formData);
      console.log(formData.id);
      let data = {id: this.blog.id, formdata: formData}
      this.$store.dispatch("updateBlog", data);
    },
    getFile(event) {
      this.blogImg = event.target.files[0];
      console.log(this.blogImg);
    },
    blogFill() {
      let id = this.$route.params.id;
    //   console.log(id);
      this.blog = this.blogs.filter((b) => {
        return b.id == id;
      })[0];
    //   console.log(this.blog);
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
.old-img {
    max-width: 200px;
    max-height: 200px;
}
</style>